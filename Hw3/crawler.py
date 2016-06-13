#This is a crawler program about crawl the web page
#and extract the email addresses from all the web pages 
#reachable from that web site.
#20160531 by HKK
#git hub link:https://github.com/aa40105/CCU_python/tree/master/Hw3

import os,sys,requests,time,glob
from bs4 import BeautifulSoup

#sys.argv[1] = "http://www.cs.ccu.edu.tw/members/lish?phpgrade=ms104&link=1"

url_list = []
mail_list = []
global starturl

def crawlerLink (url):
	#print(starturl)
	res = requests.get(url)
	soup = BeautifulSoup(res.text.encode("utf-8"),"lxml")#linux add ,lxml ; windows add html.parser
	for crawlist in soup.findAll("a",href=True):
		#print()
		catch = crawlist["href"]
		#print(type(catch))
		#print(catch)
		#print(catch.rfind("/"))
		checkurl(catch)

		#this is find mail location
		if(catch.startswith("mail")):
			mail(catch)
			#print(mail["href"])
		#time.sleep(1)
		#elif(catch.startswith("https:")):
def checkurl (url):
	tmpurl = starturl[0:starturl.rindex("/")]
	#print(url)

	if (url.startswith("http://")):
		url = url
		#if(starturl != url):
		if ((starturl == url)and (url not in url_list)):
			url_list.append(url)
	
	elif (url.startswith("./")):
		url = sys.argv[1] + url.strip("./")
		if (url not in url_list):
			url_list.append(url)

	elif (url.startswith("../")):
		url = sys.argv[1] + url.strip("../")
		if (url not in url_list):
			url_list.append(url)

	elif (url.startswith("/")):
		url = url.lstrip("/")
		url = sys.argv[1] + url
		if (url not in url_list):
			url_list.append(url)

	elif (url.startswith("list.php?")):
		url = sys.argv[1] + "members/" + url
		if (url not in url_list):
			url_list.append(url)
	else :
		url = sys.argv[1] + url 
		if (url not in url_list):
			url_list.append(url)
		

	#remove we don't need url		
	#elif (url.startswith("#")):
	for x in url_list:
		if(x.rfind("pdf") > 0):
			url_list.remove(x)
		elif(x.rfind("htm") > 0):
			url_list.remove(x)
		elif(x.rfind("mail") > 0):
			url_list.remove(x)
		elif(x.rfind("doc") > 0):
			url_list.remove(x)
		elif(x.rfind("#") == len(x) - 1):
			url_list.remove(x)
		elif(x.rfind("flv") > 0):
			url_list.remove(x)
		elif(x.rfind("ppt") > 0):
			url_list.remove(x)
		elif(x.rfind("jpg") > 0):
			url_list.remove(x)
		elif(x.rfind("zip") > 0):
			url_list.remove(x)
		elif(x == "http://www.cs.ccu.edu.tw/index.php"):
			url_list.remove(x)
		elif(x == sys.argv[1]):
			url_list.remove(x)

def mail(mail):
	
	if(mail.startswith("mailto:")):
		x = mail.rindex(":")
		mail = mail[x + 1:len(mail)]
		if (mail not in mail_list):
			mail_list.append(mail)
	
	elif(mail.startswith("mail:")):
		x = mail.rindex(":") 
		mail = mail[x + 1:len(mail)]
		if (mail not in mail_list):
			mail_list.append(mail)
	
	
if __name__ == "__main__":

	if (len(sys.argv) == 1):
		print("Usage: python3 crawler.py [hostname]")
		sys.exit(0)
	originurl = sys.argv[1]
	starturl = sys.argv[1]
	txturl = originurl[originurl.index("w"):len(originurl)-1] + ".txt"
	#print(txturl)
	secondcount = 0
	mailcount = 1
	#if(os.path.isfile(txturl) == "True"):
	#	f = open(txturl,"r")
	#	print(f.read())
	#	f.close()
	#	sys.exit()

	crawlerLink(starturl)
	url_count = len(url_list)
	#print(url_count)
	#test second layer
	
	crawlerLink(url_list[0])
	crawlerLink(url_list[1])
	
	for x in range(0,len(url_list),1):
		temp_url = url_list[x]
		print(temp_url)
		crawlerLink(temp_url)

#	for x in range(url_count,len(url_list)- 1,1):
#		temp_url = url_list[x]
#		crawlerLink(temp_url)
	
	for x in range(0,len(url_list)- 1,1):
		temp_url = url_list[x]
		crawlerLink(temp_url)

	#test url list
	#print("\n\n")
	for y in url_list:
		print(y)

	#test mail list
	f = open(txturl,'w')
	for x in mail_list:
		y =str(mailcount) + ":" + x + "\n"
		f.write(y)
		print(x)
		mailcount +=1
	f.close()

	#print("numbers of mail:" )
	print(len(mail_list))
	#print(url_count)
