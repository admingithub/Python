import requests
import time
import re
import os
import os.path
import _thread
from urllib import request
from bs4 import BeautifulSoup
import urllib3

#禁用安全请求警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def gethtml(url,header):
	session = requests.Session()
	if(header==""):
		return session.get(url).text
	else:
		return session.get(url,headers=header).text

def downmp3(url,filename):
	path="D:\\Python\\163music\\"+filename
	request.urlretrieve(url,path)

def download_file(mp3_url,file_folder,filename):
	#文件夹不存在创建文件夹
	path="D:\\Python\\163music\\"+file_folder
	folder=os.path.exists(path)
	file=path+"\\"+filename
	if not folder:
		os.makedirs(path)
	else:
		if os.path.exists(file):
			return
	_head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
	try:
		rs = requests.get(mp3_url,headers=_head,allow_redirects=False,verify=False)
		newurl=rs.headers["Location"]
		print("下载文件："+filename)	
		request.urlretrieve(newurl, path+"\\"+filename)
	except Exception:
		print("获取文件异常："+filename)

cookie="_iuqxldmzr_=32;"
Host="music.163.com"
Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
headers={"Cookie":cookie,"Host":Host,"User-Agent":Agent}

url="https://music.163.com/discover/toplist"
ids=["19723756","3779629","2884035","3778678","2534472105","1978921795","2250011882","2006508653"]
dires=["云音乐飙升榜","云音乐新歌榜","网易原创歌曲榜","云音乐热歌榜","国风风云榜","云音乐电音榜","抖音排行榜","电竞音乐榜"]


index=0
while index<len(ids):
	dire=dires[index]
	url="https://music.163.com/discover/toplist?id="+ids[index]
	html=gethtml(url,headers)
	bs=BeautifulSoup(html,"html.parser")
	for song in bs.find("ul",class_="f-hide").children:	
		title=song.a.text.strip()
		songurl="https://music.163.com"+song.a["href"]	
		#https://music.163.com/song?id=1325702742
		id=songurl.split('=')[1]
		downurl="https://music.163.com/song/media/outer/url?id=" + id + ".mp3";
		download_file(downurl,dire,title+".mp3")
		# _thread.start_new_thread(download_file, (downurl,dire,title+".mp3"))
	index=index+1
