#!/usr/bin/env
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import sys
import os
import time
reload(sys)
sys.setdefaultencoding('utf8')

url='somewebsite'



def go_to_text(browser):
	press_text=WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content-html')))
	press_text=browser.find_element_by_css_selector('#content-html')
	press_text.click()

#csgModal > div.csg-modal > header > a.csg-modal-btn.csg-modal-close > span

def close_window(browser):
	try:
		press_x=WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#csgModal > div.csg-modal > header > a.csg-modal-btn.csg-modal-close > span')))
		press_x=browser.find_element_by_css_selector('#csgModal > div.csg-modal > header > a.csg-modal-btn.csg-modal-close > span')
		press_x.click()
	except:
		pass

def login(browser,url):
	browser.get(url)
	username=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#user_login')))
	username=browser.find_element_by_css_selector('#user_login')
	username.send_keys('someusername')
	password=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#user_pass')))
	password=browser.find_element_by_css_selector('#user_pass')
	password.send_keys('somepassword')
	submit=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#wp-submit')))
	submit=browser.find_element_by_css_selector('#wp-submit')
	submit.click()

def go_to_page(browser):
	pages=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#menu-pages > a > div.wp-menu-name')))
	pages=browser.find_element_by_css_selector('#menu-pages > a > div.wp-menu-name')
	pages.click()
	addpages=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#wpbody-content > div.wrap > h1 > a')))
	addpages=browser.find_element_by_css_selector('#wpbody-content > div.wrap > h1 > a')
	addpages.click()

def title_wp(browser,title):
	actions = ActionChains(browser)
	pagetitle=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'title')))
	pagetitle=browser.find_element_by_id('title')
	pagetitle.click()
	pagetitle.send_keys(title)
	# actions.move_to_element(pagetitle).send_keys(Keys.NULL).perform()
	# actions.move_to_element(pagetitle).send_keys(title).perform()




def save_as_draft(browser):
	save_as_draft=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#save-post')))
	save_as_draft=browser.find_element_by_css_selector('#save-post')
	save_as_draft.click()

def page_template(browser):
	page_template=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#page_template')))
	page_template=browser.find_element_by_css_selector('#page_template')
	browser.execute_script("arguments[0].click();", page_template)
	page_template.send_keys('Blank - No container | No Header, No Footer')

def title_seo(browser,seotitle):
	pagetitle=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#aiosp_title_wrapper > div > span.aioseop_option_input > div.aioseop_option_div > input[type="text"]:nth-child(1)')))
	pagetitle=browser.find_element_by_css_selector('#aiosp_title_wrapper > div > span.aioseop_option_input > div.aioseop_option_div > input[type="text"]:nth-child(1)')
	pagetitle.send_keys(seotitle)


def description_seo(browser,description):
	description_element=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#aiosp_description_wrapper > div > span.aioseop_option_input > div.aioseop_option_div > textarea')))
	description_element=browser.find_element_by_css_selector('#aiosp_description_wrapper > div > span.aioseop_option_input > div.aioseop_option_div > textarea')
	description=description.replace('\n',' ')
	description_element.send_keys(str(description))

def keyword_seo(browser,keyword,town,city):
	keyword_element=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#aiosp_keywords_wrapper > div > span.aioseop_option_input > div.aioseop_option_div > input[type="text"]')))
	keyword_element=browser.find_element_by_css_selector('#aiosp_keywords_wrapper > div > span.aioseop_option_input > div.aioseop_option_div > input[type="text"]')
	my_string=keyword+', '+keyword+' '+town+', '+keyword+' '+city+', '+keyword+' '+town+' '+city
	keyword_element.send_keys(my_string)


def split(word):
	words=[x.strip() for x in word.split(',')]
	return words

def read_text():
	text1=open('sample.txt','r')
	text=text1.read()
	text = unicode(text, errors='ignore')
	text=text.encode('utf-8').strip()
	text=text.encode("ascii","ignore")
	text1.close()
	return text


def replace_lists():
	list_keywords=list()
	list_towns=list()
	list_cities=list()
	list_states=list()
	text1=open('keywords.txt','r')
	text2=open('towns.txt','r')
	text3=open('cities.txt','r')
	text4=open('states.txt','r')
	for line in text1:
		list_keywords.append(line)
	for line in text2:
		list_towns.append(line)
	for line in text3:
		list_cities.append(line)
	for line in text4:
		list_states.append(line)
	text1.close()
	text2.close()
	text3.close()
	text4.close()
	return list_keywords,list_towns, list_cities,list_states

def replace(text,town,city,keyword,state):
	if '<town>' in text:
		text=text.replace('<town>',town)
	if '<city>' in text:
		text=text.replace('<city>',city)
	if '<keyword>' in text:
		text=text.replace('<keyword>',keyword)
	if '<state>' in text:
		text=text.replace('<state>',state)
	return text


def write_to_visual(browser,text):
	#content-tmce
	click_visual=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content-tmce')))
	click_visual=browser.find_element_by_css_selector('#content-tmce')
	click_visual.click()
	send_text=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#content_ifr')))
	send_text=browser.find_element_by_css_selector('#content_ifr')
	text=text.replace('\n\n','\n ')
	send_text.send_keys('[')
	send_text.send_keys(str(text))


def get_title():
	text=open('title.txt','r')
	title=text.read()
	text.close()
	return title

def get_seo_title():
	text=open('seotitle.txt','r')
	seotitle=text.read()
	text.close()
	return seotitle

def get_description():
	text=open('description.txt','r')
	description=text.read()
	description=str(description)
	text.close()
	return description

def press_publish(browser):
	publish_but=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#publish')))
	publish_but=browser.find_element_by_css_selector('#publish')
	publish_but.click()



def main(browser,title,seotitle,description,url,keyword,town,city,state):
	text=read_text()
	title=replace(title,town,city,keyword,state)
	
	seotitle=replace(seotitle,town,city,keyword,state)
	description=replace(description,town,city,keyword,state)
	text=replace(text,town,city,keyword,state)
	go_to_page(browser)

	close_window(browser)
	title_wp(browser,title)
	time.sleep(10)
	close_window(browser)
	# save_as_draft(browser)
	page_template(browser)
	close_window(browser)
	# save_as_draft(browser)
	title_seo(browser,seotitle)
	close_window(browser)
	description_seo(browser,description)
	close_window(browser)
	keyword_seo(browser,keyword,town,city)
	close_window(browser)#csgModal > div.csg-modal > header > a.csg-modal-btn.csg-modal-close > span
	browser.execute_script("window.scrollTo(0, 0)")
	close_window(browser)
	write_to_visual(browser,text)
	close_window(browser)
	browser.execute_script("window.scrollTo(0, 0)")
	close_window(browser)
	press_publish(browser)
	



keyword,town,city,state=replace_lists()
title=get_title()
seotitle=get_seo_title()
description=get_description()
browser=webdriver.Chrome()
browser.maximize_window()
login(browser,url)
for i in range(0,len(keyword)):
	if __name__ == "__main__":
		main(browser,title,seotitle,description,url,keyword[i],town[i],city[i],state[i])

browser.close()