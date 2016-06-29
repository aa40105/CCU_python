import os,sys,requests,time,glob,urllib
from bs4 import BeautifulSoup
import modify

#use  soup = download( url,title)
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
	soup = BeautifulSoup(res.text,"html.parser")
	#soup = BeautifulSoup(res.text.encode("utf-8"),"html.parser")
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

#modify.modify(soup,title)
	
