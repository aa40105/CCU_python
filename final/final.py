import time
import cmh
import modify,download

mon = time.localtime().tm_mon
day = time.localtime().tm_mday
page_list = []
url_list = []
title_list = []
pop_list = []
index_list = []
y = 0
cmh.get_article_url(page_list, url_list, title_list, pop_list, index_list)

for x in url_list:
	catch = title_list[y]
	index =str(index_list[y])
	title_list[y] =catch[1:len(catch)-1] +"_"+str(index_list[y])
	
	try:
		soup = download.download(x,title_list[y])
		modify.modify(soup,title_list[y])
		y +=1
	except:
		pass
