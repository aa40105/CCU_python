#This is a crawler program about crawl the web page
#and extract the email addresses from all the web pages 
#reachable from that web site.
#20160531 by HKK
#git hub link:https://github.com/aa40105/CCU_python/tree/master/Hw3

import os,sys,requests,time
from bs4 import BeautifulSoup


url_list = []
mail_list = []
global starturl

def crawlerLink (url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text.encode("utf-8"),"html.parser")#linux add ,lxml ; windows add html.parser
	for mail in soup.findAll("a",href=True):
		#print()
		catch = mail["href"]
		#print(type(catch))
		#print(catch)
		#print(catch.rfind("/"))
		checkurl(catch)

		#this is find mail location
		#if(catch.startswith("mail")):
		#	print(mail["href"])
		#time.sleep(1)
		#elif(catch.startswith("https:")):
		#	print("")
		#elif(catch.startswith("/")):
		#	print(sys.argv[1] + catch)
		#else :
		#	print(sys.argv[1] + "/" + catch + "\n")
		#	#crawlerParse(sys.argv[1] + "/" + catch)

def checkurl (url):
	if (url.startswith("/")):
		url = sys.argv[1] + url.strip("/")
		#print(url)
		if (url not in url_list):
			url_list.append(url)
	elif (url.startswith("./")):
		url = sys.argv[1] + url.strip("./")
		if (url not in url_list):
			url_list.append(url)
	elif (url.startswith("index2.php")):
		url = sys.argv[1] + url
		if (url not in url_list):
			url_list.append(url)
	elif (url.startswith("english")):
		url = sys.argv[1] + url
		if (url not in url_list):
			url_list.append(url)
	elif (url.startswith("https:")):
		url = url
		#if(starturl != url):
		if ((starturl == url) and(url not in url_list)):
			url_list.append(url)
			
	elif (url.startswith("mail")):
		if (url not in mail_list):
			mail_list.append(url)
	#elif (url.startswith("#")):
	for x in url_list:
		if(x.rfind("pdf") > 0):
			url_list.remove(x)
		if(x.rfind("htm") > 0):
			url_list.remove(x)

def mail():
	print("test mail")	
	
if __name__ == "__main__":

	#print(sys.argv[1])#url
	if (len(sys.argv) == 1):
		print("Usage: python3 crawler.py [hostname]")
		sys.exit(0)
	starturl = sys.argv[1]
	crawlerLink(starturl)

	#secondurl = url_list[0]
	#crawlerLink(secondurl)
	#secondurl = url_list[1]
	#crawlerLink(secondurl)
	for x in url_list:
		#print(type(x))
		#print(x)
		#secondurl = x.strip()
		crawlerLink(x)
	for y in url_list:
		print(y)



