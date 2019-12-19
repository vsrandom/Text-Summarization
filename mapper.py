import sys 
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
import os
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
np.random.seed(2018)
import nltk

stemmer = SnowballStemmer("english")

def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(token) #result.append(lemmatize_stemming(token))
    return result

total_content=""
for line in sys.stdin:
	content=line.replace('\n', '')
	total_content+=content


sentences_tokens = nltk.sent_tokenize(total_content)
templist=[]
for sentence in sentences_tokens:
	sentence=preprocess(sentence)
	templist.append(sentence)

for item in templist:
	print(str(item)+'\tc1')

