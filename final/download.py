import os,sys,requests,time,glob,urllib
from bs4 import BeautifulSoup

test = "https://www.ptt.cc/bbs/Gossiping/M.1466480440.A.8FA.html"
url = "https://images.ptt.cc/v2.17/bbs-common.css"
title = "[新聞] 稻草這樣燒就對了 生物炭減大氣碳"

def download(url,title):
	payload = {
	'from':test,
	'yes':'yes'
	}
	rs = requests.session()
	res = rs.post("https://www.ptt.cc/ask/over18",verify = False, data = payload)
	res = rs.get(test,verify = False)
	soup = BeautifulSoup(res.text,"html.parser")
	directory = title + "_file"
	directory1 = title.replace(" ","\ ") + "_file"
	#check directory exists
	if(os.path.exists(directory) == True):
		os.system("wget -qNP " + directory1 + " " +  url)
	else:
		os.mkdir(directory)
		os.system("wget -qNP " + directory1 + " " +  url)
	
	out = urllib.parse.quote(title + "_file")
	#print(out)

	#main html
	fp = open(title + ".html","wb")
	fp.write(soup.prettify("utf-8"))
	fp.close()


download(url,title)
	
