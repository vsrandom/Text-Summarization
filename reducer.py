import sys
import ast
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
import os
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
np.random.seed(2018)
import nltk


processed_docs=[]
for line in sys.stdin:
	key,value=line.split('\t')
	key = ast.literal_eval(key)
	processed_docs.append(key)

dictionary = gensim.corpora.Dictionary(processed_docs)
bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]
nt=20
lda_model = gensim.models.LdaModel(bow_corpus, num_topics=nt, \
                                  id2word=dictionary, \
                                  passes=4, alpha=[0.01]*nt, \
                                  eta=[0.01]*len(dictionary.keys()))

for i,topic in lda_model.show_topics(formatted=True, num_topics=nt, num_words=10):
    print(str(i)+": "+ topic)
    print()
