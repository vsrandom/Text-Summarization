##### Code by Vivek Sharma #####


from urllib import request
from bs4 import BeautifulSoup as bs
import re
import nltk

import heapq

url= "https://en.wikipedia.org/wiki/Machine_Learning"
allParagraphContent=""

htmlDoc=request.urlopen(url)
soupObject = bs(htmlDoc,'html.parser')
paragraphContents=soupObject.findAll('p')

for paragraphContent in paragraphContents:
	allParagraphContent += paragraphContent.text
	#print(allParagraphContent)


allParagraphContent_cleanedData=re.sub(r'\[[0-9]*\]',' ',allParagraphContent)   #removing all the boxex with numbers eg [24] etc
allParagraphContent_cleanedData=re.sub(r'\s+',' ',allParagraphContent_cleanedData) #remove continous lot of spaces

sentences_tokens = nltk.sent_tokenize(allParagraphContent_cleanedData)

allParagraphContent_cleanedData=re.sub(r'[^a-zA-Z]',' ',allParagraphContent_cleanedData)
allParagraphContent_cleanedData=re.sub(r'\s+',' ',allParagraphContent_cleanedData)



word_tokens = nltk.word_tokenize(allParagraphContent_cleanedData)

stopwords = nltk.corpus.stopwords.words('english')  #stop words are like and , the , is , for etc

word_frequencies = {}

for word in word_tokens:
	if word not in stopwords:
		if word not in word_frequencies.keys():
			word_frequencies[word]=1;
		else:
			word_frequencies[word]+=1

print(word_frequencies)
maximum_frequency_word = max(word_frequencies.values())
# calculating weighted freq of each word
for word in word_frequencies.keys() :
	word_frequencies[word] = (word_frequencies[word]/maximum_frequency_word)


# calculating scores of each sentences 

sentences_scores = {}
 # calculating sentence scores 
for sentence in sentences_tokens :
	for word in nltk.word_tokenize(sentence.lower()):
		if word in word_frequencies.keys():
			if(len(sentence.split(' '))) < 30:
				if sentence not in sentences_scores.keys():
					sentences_scores[sentence] = word_frequencies[word]
				else : 
					sentences_scores[sentence] += word_frequencies[word]


#print(sentences_scores)
#using max heap to get top sentences with highest scores
summary = heapq.nlargest(10,sentences_scores,key=sentences_scores.get)
print(summary)