#This is a crawler program about crawl the web page
#and extract the email addresses from all the web pages 
#rachable from that web site.
#20160531 by HKK
#git hub link:https://github.com/aa40105/CCU_python/tree/master/Hw3

import os,sys,requests,time
from bs4 import BeautifulSoup


url_list = []
def crawlerParse (url):
	res = requests.get(sys.argv[1])
	soup = BeautifulSoup(res.text.encode("utf-8"),"html.parser")#linux add ,lxml ; windows add html.parser
	for mail in soup.findAll("a"):
		catch = mail["href"]
		#print(catch)
		checkurl(catch)
		if(catch.startswith("mail")):
			print(mail["href"])
		#time.sleep(1)
		#elif(catch.startswith("https:")):
		#	print("")
		#elif(catch.startswith("/")):
		#	print(sys.argv[1] + catch)
		#else :
		#	print(sys.argv[1] + "/" + catch + "\n")
		#	#crawlerParse(sys.argv[1] + "/" + catch)
#20160607 test catch under page
def checkurl (url):
	if (url.startswith("/")):
		url = sys.argv[1] + url
		print(url)
	elif (url.startswith("./")):
		url = sys.argv[1] + url.strip("./")
	elif (url.startswith("index2.php")):
		url = sys.argv[1] + url
	elif (url.startswith("english")):
		url = sys.argv[1] + url
	elif (url.startswith("https:")):
		url = url
	if (url not in url_list):
		#url_list.append(url)
		print(url)
		#print("check")
		#for x in url_list:
		#	print(url_list)	
	
if __name__ == "__main__":

	#print(sys.argv[1])#url
	#res = requests.get(sys.argv[1])parse
	if (len(sys.argv) == 1):
		print("Usage: python3 crawler.py [hostname]")
		sys.exit(0)
	crawlerParse(sys.argv[1])




