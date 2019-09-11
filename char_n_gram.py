# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 19:33:14 2019

@author: Anuraag
"""

import random

text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

n = 6  #trigram model

ngrams = {}

#Create the n grams
for i in range(len(text)-n):
    gram = text[i:i+n]
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(text[i+n])
    


# testing
current_gram = text[0:n]
result = current_gram
for i in range(100):
    if current_gram not in ngrams.keys():
        break
    pos = ngrams[current_gram]
    next_item = pos[random.randrange(len(pos))]
    result += next_item
    current_gram = result[len(result)-n:len(result)]
    
print(result)