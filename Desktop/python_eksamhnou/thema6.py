#!/usr/bin/env python
import datetime as dt
import urllib2 as url

i=raw_input('date\n')
try:
	dt.datetime.strptime(i,'%d-%m-%Y')
except ValueError:
	print "wrong format"

#print i
prefix='http://applications.opap.gr/DrawsRestServices/kino/drawDate/'
surfix='.json'
request=url.Request(prefix+i+surfix)
response=url.urlopen(request)
opap=response.read()
#print opap
opap=opap.strip()
opap=opap.replace('{"drawTime"','\n{"drawTime"')
opap=opap.replace('[','')
opap=opap.replace('{','')
opap=opap.replace(']','')
opap=opap.replace('}','')
opap=opap.replace(',','')
opap=opap.replace('"','')
opap=opap.replace('drawNo','\t    drawNo')
opap=opap.replace('results',' results')
#print opap
noumera=[]
start=opap.find('results:')
end=opap.find('\n',start)
for i in range(0,2):
	noumera.append(opap[start:end])
	start1=opap.find(end)
	end1=opap.find('\n',start1)
	noumera.append(opap[start1:end1])
print noumera[1]