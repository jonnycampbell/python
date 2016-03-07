#!/usr/bin/env python
import datetime as dt
import urllib2 as url
import tweepy
consumer_key='JqK4GdtB3JhEWPyPyofmQqtOW'
consumer_secret='qFdrqRzNdMsBu81Hg0p286RnzZVAGnakgnepTmFcaYcrhcWf7C'
access_token='413525218-K44QPskEZpu4fPX1aR2fwzgIVwEwxmyopzV0tbBj'
access_token_secret='1ItrLvOs7n4RkB03qYOlKgsW7yjPAjNCM5u92i1v6TnwB'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth)

onoma=raw_input("Give twitter username: \n")
user=api.get_user(onoma)
followers1=user.followers_count
status1=user.statuses_count
following1=user.friends_count
liks1=user.favourites_count


onoma2=raw_input("Give anotha twitter username: \n")
user2=api.get_user(onoma2)
followers2=user2.followers_count
status2=user2.statuses_count
following2=user2.friends_count
liks2=user2.favourites_count

counter1=0
counter2=0

if(followers1>followers2):
	counter1+=1
else:
	counter2+=1

if(status1>status2):
	counter1+=1
else:
	counter2+=1

if(following1>following2):
	counter1+=1
else:
	counter2+=1

if(liks1>liks2):
	counter1+=1
else:
	counter2+=1

print "Ta profil einai etoima: "
print "\tonoma: ",onoma,"tweets",status1,"followers: ",followers1,"following: ",following1,"likes: ",liks1

print "\n\tonoma: ",onoma2,"tweets",status2,"followers: ",followers2,"following: ",following2,"likes: ",liks2

if(counter1>counter2):
	print "To profil tou", onoma,"nikaei to profil tou user",onoma2,"me skor", counter1, counter2
elif(counter1==counter2):
	print "Ta 2 profil einai isovathma"
else:
	print "To profil tou", onoma2,"nikaei to profil tou user",onoma,"me skor", counter2, counter1