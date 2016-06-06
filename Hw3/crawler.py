#This is a crawler program about crawl the web page
#and extract the email addresses from all the web pages 
#rachable from that web site.
#20160531 by HKK
#git hub link:https://github.com/aa40105/CCU_python/tree/master/Hw3

import os,sys,requests
from bs4 import BeautifulSoup

def crawlerParse (url):
	res = requests.get(sys.argv[1])
	soup = BeautifulSoup(res.text,"html.parser")#linux add ,lxml ; windows add html.parser
	for mail in soup.findAll("a"):
		catch = mail["href"]
		#print(catch)
		if(catch.startswith("mail")):
			print(mail["href"])
		#elif(catch.startswith("https:")):
		#	print("")
		elif(catch.startswith("/")):
			print(sys.argv[1] + catch)
		#else :
		#	print(sys.argv[1] + "/" + catch + "\n")
		#	#crawlerParse(sys.argv[1] + "/" + catch)

#20160607 test catch under page
if __name__ == "__main__":

	#print(sys.argv[1])#url
	#res = requests.get(sys.argv[1])parse
	if (len(sys.argv) == 1):
		print("Usage: python3 crawler.py [hostname]")
		sys.exit(0)
	crawlerParse(sys.argv[1])




