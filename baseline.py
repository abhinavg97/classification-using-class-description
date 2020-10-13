import numpy as np

from tweet_classification.utils import read_classes, read_df, vectorize_text, cosine


dataset_df = read_df("data/Fire16/fire16_data.csv")

label_df = read_classes("data/Fire16/fire16_labels.txt")


label_df.to_csv("data/Fire16/fire16_processed_labels.csv", index=0)
dataset_df.to_csv("data/Fire16/fire16_processed_data.csv", index=0)

print(dataset_df)
print(label_df)

label_vectors = list(map(lambda narrative: vectorize_text(narrative), label_df["narrative"].tolist()))
labels = label_df["title"].tolist()


for index, doc_row in dataset_df.iterrows():

    target = doc_row['labels']

    doc = doc_row['tweets']

    doc_vector = vectorize_text(doc)

    label_scores = np.array(list(map(lambda label_vector: cosine(doc_vector, label_vector), label_vectors)))

    print(np.nonzero(label_scores), target)
