# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:15:13 2026

@author: Inspector
"""

#108.removing stop words
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

en_stopwords=stopwords.words('english')
print(en_stopwords)

sentence='the cat is sleeping on the mat because it was so tired'
sentence_no_stopwords=' '.join([word for word in sentence.split() if word not in en_stopwords])
print(sentence_no_stopwords)

newsentence="if the word not in the list remove he word completely"
newsentence_no_words=" ".join([word for word in newsentence.split() if word not in en_stopwords ]) 
print(newsentence_no_words)

A="this is my beautifull house in the vally of Azad Jammu And Kashmir"
s_no_stopwords=' '.join([word for word in A.split() if word not in en_stopwords])
print(s_no_stopwords)

en_stopwords.remove("in")
en_stopwords.remove("this")
en_stopwords.append("go")

new=" ".join([word for word in A.split() if word not in en_stopwords])
print(new)