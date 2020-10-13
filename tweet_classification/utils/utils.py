import re
import spacy
import gensim
import numpy as np
import pandas as pd
from ast import literal_eval


from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


from .text_processing import TextProcessing


nlp = spacy.load('en_core_web_sm')


def read_df(dataset_path, text_processor=TextProcessing()):
    df = pd.read_csv(dataset_path, index_col=0)
    df['labels'] = list(map(lambda label_list: literal_eval(label_list), df['labels'].tolist()))
    df['tweets'] = list(map(lambda tweet: text_processor.process_text(tweet), df['tweets'].tolist()))
    return df


def read_classes(class_path, text_processor=TextProcessing()):
    """
    Reads class id, title, description and narrative and stores in a dataframe
    Args:
        class_path ([type]): [description]
    """
    count = 0
    data_row = []

    with open(class_path, "r") as file1:
        for line in file1:
            stripped_line = line.strip()
            if count % 4 == 0:
                index = int(stripped_line)
            elif count % 4 == 1:
                title = text_processor.process_text(stripped_line)
            elif count % 4 == 2:
                desc = text_processor.process_text(stripped_line)
            elif count % 4 == 3:
                narrative = text_processor.process_text(stripped_line)
                data_row += [[index, title, desc, narrative]]
            count += 1
    parsed_data = pd.DataFrame(data_row, columns=['id', 'title', 'desc', 'narrative'])

    parsed_data['narrative'] = remove_common_narrative_intersection(parsed_data['narrative'].tolist())
    # parsed_data['narrative'] = add_synonyms_from_intersection(parsed_data['narrative'].tolist(), parsed_data['desc'].tolist())
    return parsed_data


def remove_common_narrative_intersection(docs):

    vectorizer = TfidfVectorizer()
    vectorizer.fit_transform(docs)
    feature_names = vectorizer.get_feature_names()
    remove_words = {}
    idf_scores = vectorizer.idf_

    for i, feature in enumerate(feature_names):
        if idf_scores[i] < 1.3:
            remove_words[feature] = 1

    for index in range(len(docs)):
        for word in remove_words:
            docs[index] = re.sub(word, '', docs[index])

    return docs


def add_synonyms_from_intersection(list1, list2):

    model = gensim.models.KeyedVectors.load_word2vec_format('data/crisisNLP_word2vec/crisisNLP_word_vector.bin', binary=True)
    return_list = list1[:]

    word_to_sym = {}
    for i in range(len(list1)):

        narrative = list1[i]
        desc = list2[i]

        intersection = list(set(narrative.split(" ")) & set(desc.split(" ")))

        for word in intersection:
            synonyms = model.most_similar(positive=[word], negative=[], topn=10)
            # synonyms = []
            # for syn in wordnet.synsets(word):
            #     for lemma in syn.lemmas():
            #         synonyms.append(lemma.name())
            return_list[i] += " " + " ".join(set(synonyms)) + " "
            word_to_sym[word] = list(set(synonyms))
    import json
    with open('data.json', 'w') as f:
        json.dump(word_to_sym, f)
    return return_list


def vectorize_text(doc):

    tokens = nlp(doc)
    vector = np.zeros(len(tokens[0].vector))
    for token in tokens:
        vector += token.vector

    vector /= len(doc)

    return vector


def cosine(vector1, vector2):

    return cosine_similarity([vector1], [vector2])[0][0]
