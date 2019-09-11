# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:15:17 2019

@author: Anuraag
"""

from nltk.corpus import wordnet

syno = []
anto = []

for syn in wordnet.synsets("good"):
    for s in syn.lemmas():
        syno.append(s.name())
        for a in s.antonyms():
            anto.append(a.name())

print(set(syno))
print(set(anto))