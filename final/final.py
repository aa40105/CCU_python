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
#cmh.print_list(url_list, title_list, pop_list, index_list)



for x in url_list:
	catch = title_list[y]
	index =str(index_list[y])
	title_list[y] =catch[1:len(catch)-1] +"_"+str(index_list[y])
	#catch = str(index_list[y])
	#soup = download.download(x,catch)
	soup = download.download(x,title_list[y])
	modify.modify(soup,title_list[y])
	#modify.modify(soup,catch)
	y +=1



"""
test1 = [1,2,3,4,5,6,7,8,9,0]
print(test1)

test2 = list(test1)
print(test2)

test1.reverse()

test3 = []
test3.extend(test1)
print(test3)

test3.extend(test1)
print(test3)
"""

