# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 03:32:26 2026

@author: Inspector
"""

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize

#sentence tokenization 
Sentences='Her name is luna. she is a good girl'

senttt=sent_tokenize(Sentences)
print(senttt)

text='this is me'
sentt=word_tokenize(text)
print(sentt)
     
cahr_token=list(text )
print(cahr_token)


sentence_2 = "Her cat's name is Luna and her dog's name is max"

word_tokenize(sentence_2.lower())