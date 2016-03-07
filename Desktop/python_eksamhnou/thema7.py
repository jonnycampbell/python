#!/usr/bin/env python
#from urllib2 import Request, urlopen, URLError
import urllib2
lat=raw_input('give lattitude please: \n')
lon=raw_input('give longtitude: \n')

prefix='http://api.openweathermap.org/data/2.5/weather?lat='
prefix2='&lon='
appid='&APPID=9e539432e609b9569d4772f3ca2bf3ab'


request=urllib2.Request(prefix+lat+prefix2+lon+appid)

response = urllib2.urlopen(request)
weather = response.read()
#print weather
weather=weather.strip()
weather=weather.replace(",","\n")
weather=weather.replace("{","")
weather=weather.replace('coord":','coord":\n')
weather=weather.replace("}","")
weather=weather.replace("[","")
weather=weather.replace("]","")
print weather
start=weather.find('temp')
end=weather.find('\n',start)
temp=weather[start:end]
temp=temp.replace('temp":','')
start1=weather.find('"name"')
end1=weather.find('\n',start1)
city=weather[start1:end1]
city=city.replace('"name"','')
print "H thermokrasia se kelvin einai: ", temp
temp=float(temp)-273.15
print "h thermokrasia sth polh",city, "einai: ", temp,"C"
if temp>20:
	print"NICE"
elif temp<5:
	print"brrr"

