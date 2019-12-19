import os
import re
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
np.random.seed(2018)
import nltk
import heapq

path1="/home/vivi/Desktop/TextSum/c1"
path2="/home/vivi/Desktop/TextSum/c2"

total_content=""
for filename in os.listdir(path1):
	file = open(path1+'/'+filename, encoding="utf8")
	content=file.read().replace('\n', '')
	total_content+=content


for filename in os.listdir(path2):
	file = open(path2+'/'+filename, encoding="utf8")
	content=file.read().replace('\n', '')
	total_content+=content

sentences_tokens = nltk.sent_tokenize(total_content)

word_frequencies = {}
file = open('out2.txt','r')
for line in file:
	word_frequencies[line.split('\t')[0].strip()]=int(line.split('\t')[1].strip('\n'))

maximum_frequency_word = max(word_frequencies.values())
print(maximum_frequency_word)

for word in word_frequencies.keys() :
	word_frequencies[word] = (word_frequencies[word]/maximum_frequency_word)


sentences_scores = {}

for sentence in sentences_tokens :
	for word in nltk.word_tokenize(sentence.lower()):
		if word in word_frequencies.keys():
			if(len(sentence.split(' '))) < 30:
				if sentence not in sentences_scores.keys():
					sentences_scores[sentence] = word_frequencies[word]
				else : 
					sentences_scores[sentence] += word_frequencies[word]




summary = heapq.nlargest(50,sentences_scores,key=sentences_scores.get)
print(summary)
