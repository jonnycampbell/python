from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import sys
import urllib
from BeautifulSoup import *
import os
import time
reload(sys)
sys.setdefaultencoding('utf8')


def only_numerics(seq):
    return filter(type(seq).isdigit, seq)


def close_popup(browser):
	try:	
		# browser.switch_to_default_content()
		# browser.switch_to_frame(browser.find_element_by_xpath('//*[@id="PopupSignupForm_0"]/div[1]/div[2]/iframe'))
		alert=browser.switch_to_alert()
		close=WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PopupSignupForm_0"]/div[1]/div[1]')))
		close=browser.find_element_by_xpath('//*[@id="PopupSignupForm_0"]/div[1]/div[1]')
		close.click()
	except Exception as E:
		return


def create_css_paths():
	paths=list()
	prefix='//*[@id="section-stories-container"]/div['
	postfix=']/h2/a'
	for i in range(1,300):
		paths.append(prefix+str(i)+postfix)
	return paths


def get_links(browser,paths):	
	links=list()
	for path in paths:
		try:
			# link=WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, path)))
			link=browser.find_element_by_xpath(path)
			links.append(link.get_attribute('href'))
		except Exception as E:
			print E
			pass
	return links

def get_title(browser):	
	title=WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="quote-share-container"]/div[1]/h1')))
	title=browser.find_element_by_xpath('//*[@id="quote-share-container"]/div[1]/h1').text
	return title

def get_likes(browser):	
	likes=WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="storyContentSocial"]/div[2]/div/span/a')))
	likes=browser.find_element_by_xpath('//*[@id="storyContentSocial"]/div[2]/div/span/a').text
	likes=only_numerics(likes)
	return likes

def click_pages(browser):
	number_of_pages=0
	next=WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="section-stories-container"]/a')))
	next=browser.find_element_by_xpath('//*[@id="section-stories-container"]/a')
	next.click()
	while True and number_of_pages<15:	
		try:
			next=WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="section-stories-container"]/a[1]')))
			next=browser.find_element_by_xpath('//*[@id="section-stories-container"]/a[1]')
			next.click()
			number_of_pages+=1
		except:
			break

def get_info(browser,link,text,text2):
	browser.get(link)
	title=get_title(browser)
	text.write(title.encode('utf8','ignore')+'\n')
	likes=get_likes(browser)
	text2.write(str(likes)+'\n')


url='somewebsite'

browser=webdriver.PhantomJS()
browser.maximize_window()
browser.get(url)
close_popup(browser)
time.sleep(4)
click_pages(browser)

paths=create_css_paths()
print 'Getting links'

links=get_links(browser,paths)
text=open('titles.txt','w')
text2=open('likes.txt','w')
print 'Start Gathering'
for link in links:
	try:
		get_info(browser,link,text,text2)
	except:
		pass

text.close()
text2.close()
