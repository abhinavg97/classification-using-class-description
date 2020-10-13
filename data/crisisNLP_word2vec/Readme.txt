-----------------------------
CrisisNLP Word2vec Model (V1.2)
-----------------------------

DESCRIPTION:
------------
The trained model consists of a vocabulary with size 7976291 (~7 million) and 300 dimensional vector. 


HOW TO USE IT:
--------------
For example to find the top ten most similar words to the word "shelter", use the following python code:

***
from gensim.models import word2vec
model = word2vec.Word2Vec.load_word2vec_format('crisisNLP_word_vector.bin', binary=True)
words=model.most_similar(positive=['shelter'], negative=[], topn=10)

for w in words:
  print w[0]
# Few examples of most similar words
needs
somewhere
safe
needing
gurdwara
opened
give
stranded
offering
temple

#Finding the word vector
vector = model['shelter']
***


CITATION POLICY:
----------------
If you use this tool, please cite the following paper:

"Muhammad Imran, Prasenjit Mitra, Carlos Castillo: Twitter as a Lifeline: Human-annotated Twitter Corpora for NLP of Crisis-related Messages. In Proceedings of the 10th Language Resources and Evaluation Conference (LREC), pp. 1638-1643. May 2016, Portorož, Slovenia."


@InProceedings{Imran_et_al.LREC16,
  author = {Muhammad Imran and Prasenjit Mitra and Carlos Castillo},
  title = {Twitter as a Lifeline: Human-annotated Twitter Corpora for NLP of Crisis-related Messages},
  booktitle = {Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC 2016)},
  year = {2016},
  month = {may},
  date = {23-28},
  location = {Portoroz, Slovenia},
  publisher = {European Language Resources Association (ELRA)},
  address = {Paris, France},
  isbn = {978-2-9517408-9-1},
  language = {english}
 }


Acknowledgements:
-----------------
CrisisNLP team is thankful to Dr. Firoj Alam for helping us train the crisis word2vec model.