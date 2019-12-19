import sys
import os
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
np.random.seed(2018)
import nltk



wordlist = []
file = open('/home/vivi/Desktop/TextSum/out1.txt','r')
for line in file:
	wordlist.append(line.strip('\n'))

total_content=""
for line in sys.stdin:
	content=line.replace('\n', '')
	total_content+=content

word_tokens=nltk.word_tokenize(total_content)

for word in word_tokens:
	if word in wordlist:
		print(str(word)+'\t1')


