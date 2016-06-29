import os,sys,requests,time,glob,urllib
from bs4 import BeautifulSoup
import modify

url = "https://www.ptt.cc/bbs/Gossiping/M.1466480440.A.8FA.html"
title = "[新聞] 稻草這樣燒就對了 生物炭減大氣碳"
jpg = set()
css = set()
js = set()

def download(url,title):
	payload = {
	'from':url,
	'yes':'yes'
	}
	rs = requests.session()
	res = rs.post("https://www.ptt.cc/ask/over18",verify = False, data = payload)
	res = rs.get(url,verify = False)
	soup = BeautifulSoup(res.text.encode("utf-8"),"html.parser")
	#soup = BeautifulSoup(res.text.encode("utf-8"),"lxml")
	directory = title + "_file"
	directory1 = title.replace(" ","\ ") + "_file"
	#file path encode to utf-8
	out = urllib.parse.quote(title + "_file")
	#find jpg
	for x in soup.findAll("a",href=True):
		catch = x["href"]
		#print(catch)
		if(catch.rfind("jpg") > 0):
			jpg.add(catch)
			#wget jpg
			if(os.path.exists(directory) == True):
				os.system("wget -qNP " + directory1 + " " + catch)
			else:
				os.mkdir(directory)
				os.system("wget -qNP " + directory1 + " " + catch)
	#find css
	for x in soup.findAll("link",rel=True):
		catch = x["href"]
		#print(catch)
		if(catch.rfind("css") > 0):
			catch = "https:" + catch
			css.add(catch)
			#wget css
			if(os.path.exists(directory) == True):
				os.system("wget -qNP " + directory1 + " " + catch)	
			else:
				os.mkdir(directory)
				os.system("wget -qNP " + directory1 + " " + catch)
	#find js
	for x in soup.findAll("script",src=True):
		catch = x["src"]
		if(catch.rfind(".js") > 0):
			catch = "https:" + catch
			js.add(catch)
			#wget css
			if(os.path.exists(directory) == True):
				os.system("wget -qNP " + directory1 + " " + catch)	
			else:
				os.mkdir(directory)
				os.system("wget -qNP " + directory1 + " " + catch)
	return soup
"""
def modify(soup, title):
	css = ["hkk"]
	y = 0
	directory = title + "_file"
	directory1 = title.replace(" ","\ ") + "_file"
	#file path encode to utf-8
	out = urllib.parse.quote(title + "_file")

	#css
	for x in soup.findAll("link",href = True):
		if(y>0):
			catch = x["href"]
			catch = out + catch[catch.rindex("/"):]
			x["href"] = catch
			soup.select("link")[y].replaceWith(x)
		y+=1

	#js
	z = 0
	for x in soup.findAll("script",src=True):
		catch = x["src"]
		catch = out + catch[catch.rindex("/"):]
		x["src"] = catch
		soup.select("script")[z].replaceWith(x)
		z+=1
	
	#jpg
	jpgcount = 0
	for x in soup.findAll("img",src=True):
		catch = x["src"]
		if(catch.rfind("jpg") > 0):
			catch = out + catch[catch.rindex("/"):]
			x["src"] = catch
			soup.select("img")[jpgcount].replaceWith(x)
		jpgcount +=1
	
	#main html
	fp = open(title + ".html","wb")
	fp.write(soup.prettify("utf-8"))
	fp.close()
"""
soup=download(url,title)
modify.modify(soup,title)
	
