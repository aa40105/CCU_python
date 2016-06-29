import requests
import string, time, os
from bs4 import BeautifulSoup as bsp

ask = 'https://www.ptt.cc/ask/over18'
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
test_url = 'https://www.ptt.cc/bbs/Gossiping/index15201.html'

payload = {
'from':'/bbs/Gossiping/index.html',
'yes':'yes'
}

mon = str(time.localtime().tm_mon)
day = str(time.localtime().tm_mday)
today = mon + '/' + day

pop_limit = 50

def page_handle(s, url_list, title_list, pop_list):
	
	for i in s.select('.r-ent'):
		pop = i.select('.nrec')[0].text
		date = i.select('.date')[0].text
		title = i.select('.title')[0].text
		author = i.select('.author')[0].text
		
		if('已被' not in title and '刪除' not in title and today in date):
			link = i.find('a', href = True)
			link = 'https://www.ptt.cc' + link['href']
			#print(pop, date, author, title, link, '\n')
			url_list.append(link)
			title_list.append(title)
			tmp = calc_pop(pop)
			pop_list.append(tmp)
	
def get_prev(s):
	
	for i in s.select('.btn-group-paging'):
		page_link_list = i.findAll('a', class_ = "btn wide")
		page_link = page_link_list[1]
		pre_link = page_link['href']

	pre_link = 'https://www.ptt.cc' + pre_link
	return pre_link

def calc_pop(pop):
	
	if(pop == '爆'):
		return 100
	
	elif('X' in pop):
		if('XX' in pop):
			return -100
		else:
		 	a = -10 * int(pop[1])
		 	return a
	elif(pop == ''):
		return 0
	else:
		return int(pop)

def check_today(s):

	for i in s.select('.r-ent'):
		date = i.select('.date')[0].text
		if(today in date):
			return 1
	return 0

"""
rs = requests.session()
res = rs.post(ask, verify = False, data = payload)
res = rs.get(url, verify = False)

s = bsp(res.text, "html.parser")
page_handle(s)
link = get_prev(s)

page_list = []
page_list.append(link)
#print('previous page : ' + link)
#print('today = ' + today)

for i in page_list:
	rs = requests.session()
	res = rs.post(ask, verify = False, data = payload)
	res = rs.get(i, verify = False)
	s = bsp(res.text, "html.parser")
	page_handle(s)
	print('=============',i,'==============')
	#link = get_prev(s)
	
	for j in s.select('.btn-group-paging'):
		page_link_result = j.findAll('a', class_='btn wide')
		page_link = page_link_result[1]
		page_link = page_link['href']
		link = 'https://www.ptt.cc' + page_link
	
	time.sleep(0.3)
	print('Fetching ...')
	if(check_today(s) == 1):
		page_list.append(link)

x = 0
for i in url_list:
	print(title_list[x])
	print(url_list[x])
	x = x + 1
"""

def print_list(z, y, x, index):
	# x = pop, y = title, z = url
	p = 0
	for i in x:
		print(index[p])
		print(x[p], y[p])
		print(z[p])
		p = p + 1

def index_url(url, index):
	
	count = 1
	for i in url:
		index.append(count)
		count = count + 1
	
	index.reverse()

def select_article(url_list, title_list, pop_list, index_list):

	c = 0
	url_tmp = []
	title_tmp = []
	pop_tmp = []
	index_tmp = []
	for i in index_list:
		if(pop_list[c] >= pop_limit):
			url_tmp.append(url_list[c])
			title_tmp.append(title_list[c])
			pop_tmp.append(pop_list[c])
			index_tmp.append(index_list[c])
		c = c + 1
	
	url_list.clear()
	title_list.clear()
	pop_list.clear()
	index_list.clear()
	url_list.extend(url_tmp)
	title_list.extend(title_tmp)
	pop_list.extend(pop_tmp)
	index_list.extend(index_tmp)
	
	#print_list(pop_list, title_list, url_list, index_list)


def get_article_url(page_list, url_list, title_list, pop_list, index_list):
	
	url_all = []
	title_all = []
	pop_all = []
	rs = requests.session()
	res = rs.post(ask, verify = False, data = payload)
	res = rs.get(url, verify = False)
	s = bsp(res.text, "html.parser")

	page_handle(s, url_all, title_all, pop_all)
	url_all.reverse()
	url_list.extend(url_all)
	title_all.reverse()
	title_list.extend(title_all)
	pop_all.reverse()
	pop_list.extend(pop_all)
	link = get_prev(s)
	page_list.append(link)
	
	
	for i in page_list:
		
		url_all = []
		title_all = []
		pop_all = []
		rs = requests.session()
		res = rs.post(ask, verify = False, data = payload)
		res = rs.get(i, verify = False)
		s = bsp(res.text, "html.parser")
		page_handle(s, url_all, title_all, pop_all)
		url_all.reverse()
		url_list.extend(url_all)
		title_all.reverse()
		title_list.extend(title_all)
		pop_all.reverse()
		pop_list.extend(pop_all)

		print('=============',i,'==============')

		for j in s.select('.btn-group-paging'):
			page_link_result = j.findAll('a', class_='btn wide')
			page_link = page_link_result[1]
			page_link = page_link['href']
			link = 'https://www.ptt.cc' + page_link

		time.sleep(0.3)
		print('Fetching ... ')
		if(check_today(s) == 1):
			page_list.append(link)
	
	index_url(url_list, index_list)
	select_article(url_list, title_list, pop_list, index_list)
	#print_list(pop_list, title_list, url_list, index_list)

	"""
	url_list = url_list.extend(url_all)
	title_list = title_list.extend(title_all)
	pop_list = pop_list.extend(pop_all)
	
	url_list = list(url_all)
	title_list = list(title_all)
	pop_list = list(pop_all)
	"""

"""
rs = requests.session()
res = rs.post(ask, verify = False, data = payload)
res = rs.get(url, verify = False)
s = bsp(res.text, "html.parser")

page_list = []
url_list = []
title_list = []

get_article_url(s, page_list, url_list, title_list)

print_list(title_list, url_list)
	
"""

