import os,sys,requests,time,glob,urllib
from bs4 import BeautifulSoup
#import "modify.py"

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
	soup = BeautifulSoup(res.text.encode("utf-8"),"lxml")
	directory = title + "_file"
	directory1 = title.replace(" ","\ ") + "_file"
	#file path encode to utf-8
	out = urllib.parse.quote(title + "_file")
	#find jpg
	#print(type(jpg))
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
			#print(catch)
	#find css
	for x in soup.findAll("link",rel=True):
		catch = x["href"]
		#print(catch)
		if(catch.rfind("css") > 0):
			catch = "https:" + catch
			css.add(catch)
			#print(catch)
			#wget css
			if(os.path.exists(directory) == True):
				os.system("wget -qNP " + directory1 + " " + catch)	
			else:
				os.mkdir(directory)
				os.system("wget -qNP " + directory1 + " " + catch)
	#find js
	for x in soup.findAll("script",src=True):
		catch = x["src"]
		#print(catch)
		if(catch.rfind(".js") > 0):
			catch = "https:" + catch
			js.add(catch)
			#print(catch)
			#wget css
			if(os.path.exists(directory) == True):
				os.system("wget -qNP " + directory1 + " " + catch)	
			else:
				os.mkdir(directory)
				os.system("wget -qNP " + directory1 + " " + catch)
	"""
	#main html
	fp = open(title + ".html","wb")
	fp.write(soup.prettify("utf-8"))
	fp.close()
	"""
	return soup

def modify(soup):
	css = ["hkk"]
	y = 0
	#css
	for x in soup.findAll("link",href = True):
		print(x)
		if(y>0):
			catch = x["href"]
			x["href"] = "hkk"
			soup.select("link")[y].replaceWith(x)
		print(x)
		#print(catch)
	#	print(soup.select("link").href)
		#print(x)
		#soup.select("link href"[0]).replaceWith("hkk")
		#print(soup.select("link")[y])
		#soup["link"] = "hkk"
		#print(soup.select("link")[y])
		#x = "hkk"
		#print(x)
		#soup["link"] = "hkk"
		#css.append(x)
		#print(css[y])
		y +=1
	
	#main html
	fp = open(title + ".html","wb")
	fp.write(soup.prettify("utf-8"))
	fp.close()

soup=download(url,title)
modify(soup)
	
