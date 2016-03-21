#!/usr/bin/env python
# -*- coding: utf-8 -*-

import untangle
import xlsxwriter 
import time

s=0
today=time.strftime("%d-%m-%Y")
onoma=raw_input("Give the name for the excel file. Please DO not use '.'','\n")
workbook=xlsxwriter.Workbook(onoma+"-"+today+".xlsx")
worksheet=workbook.add_worksheet()
price=list()
name=list()
availability=list()
stock=list()
temp=raw_input("Do you want to scan the website? Y/N? \n")

if(temp=="Y"):
	XML="http://spitishop.gr/skroutz.xml"
	o=untangle.parse('http://spitishop.gr/skroutz.xml')
	for product in o.skroutzstore.products.product:
		name.append(product.name.cdata)
		price.append(product.price.cdata)
		availability.append(product.availability.cdata)
		stock.append(product.instock.cdata)
		# pid=product.mpn.cdata
		s=s+1
worksheet.set_column('A:A',60)
worksheet.set_column('B:B',10)
worksheet.set_column('C:C',30)
worksheet.set_column('D:D',10)
worksheet.write(0,0,"NAME")
worksheet.write(0,1,"PRICE")
worksheet.write(0,2,"AVAILABILITY")
worksheet.write(0,3,"STOCK")
row=1
col=0
for i in range(0,len(name)):
	worksheet.write(row,col,name[i])
	worksheet.write(row,col+1,price[i])
	worksheet.write(row,col+2,availability[i])
	worksheet.write(row,col+3,stock[i])
	row=row+1

for i in range(0,len(stock)):
	if(stock[i]!='Y'):
		print "to proion", name[i],"den exei stock"

workbook.close()