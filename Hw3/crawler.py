#This is a crawler program about crawl the web page
#and extract the email addresses from all the web pages 
#rachable from that web site.
#20160531 by HKK
#git hub link:https://github.com/aa40105/CCU_python/tree/master/Hw3

import os,sys,requests
from bs4 import BeautifulSoup

#def 

if __name__ == "__main__":

	#print(sys.argv[1])#url
	#res = requests.get(sys.argv[1])parse
	if (len(sys.argv) == 1):
		print("Usage: python3 crawler.py [hostname]")
		sys.exit(0)
	res = requests.get(sys.argv[1])
	soup = BeautifulSoup(res.text,"lxml")
	#print (soup.title.text)
	for mail in soup.findAll("a"):
		catch = mail["href"]
		if(catch.startswith("mailto")):
			print(mail["href"])
	for mail1 in soup.findAll("td"):
		catch1 = mail1
		if(catch1.startswith("mail")):
			print(mail1)
	#print (soup.select("p a"))




