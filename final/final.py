import os,sys,requests,time,glob,urllib
import modify,download

url = "https://www.ptt.cc/bbs/Gossiping/M.1466480440.A.8FA.html"
title = "test"

soup = download.download(url,title)
modify.modify(soup,title)
