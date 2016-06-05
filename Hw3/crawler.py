#This is a crawler program about crawl the web page
#and extract the email addresses from all the web pages 
#rachable from that web site.
#20160531 by HKK
#git hub link:https://github.com/aa40105/CCU_python/tree/master/Hw3

import os,sys,requests
from bs4 import BeautifulSoup


if __name__ == "__main__":

	#print(sys.argv[1])#url
	#res = requests.get(sys.argv[1])parse
	res = requests.get("http://www.ee.ccu.edu.tw")
	soup = BeautifulSoup(res.text)
	#print (soup.title.text)
	for mail in soup.findAll("a"):
		print(mail["href"])
	#print (soup.select("p a"))




