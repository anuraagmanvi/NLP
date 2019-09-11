import nltk

paragraph = "The Taj Mahal was built by Shah Jahan"

words = nltk.word_tokenize(paragraph)

tagged_words = nltk.pos_tag(words)

named_ent = nltk.ne_chunk(tagged_words)

named_ent.draw()