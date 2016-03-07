#!/usr/bin/env python

import nltk
#nltk.download()
phrase1=raw_input("SAY WHAT YOU WANT! BIATCH \n")
phrase2=raw_input("EXCUSE ME DEAR SIR/MADAM. WOULD YOU MIND SAYING SOMETHING\n")
t_phrase1 = nltk.word_tokenize(phrase1)
print t_phrase1
tagged=nltk.pos_tag(t_phrase1)
print tagged[0:2]
