#!/usr/bin/env python

# import nltk
from nltk.corpus import words
import random

word_list=words.words()

rand1=random.randrange(0,236736)
rand2=random.randrange(0,236736)
# for i in range (0,236736):
# 	if(len(word_list[i])>=25):
# 		print word_list[i]

myword=word_list[rand1]

checkword=word_list[rand2]

# print len(checkword)
while(myword[len(myword)/2]!=checkword[len(checkword)/2]):
	rand2=random.randrange(0,236736)
	checkword=word_list[rand2]


print myword, checkword

new1=myword[0:len(myword)/2]
# print new1
new2=checkword[len(checkword)/2:]
# print new2
final=new1+new2
print final