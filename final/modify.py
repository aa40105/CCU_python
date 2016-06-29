import os,sys,requests,time,glob,urllib
from bs4 import BeautifulSoup

#use modify(soup,title)

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
