import requests
import time
import re
import os
import os.path
import _thread
import json
from urllib import request
from urllib.parse import quote
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

def getdownurl(song_mid):
	vkeyurl="https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey7202785251801513&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22req%22%3A%7B%22module%22%3A%22CDN.SrfCdnDispatchServer%22%2C%22method%22%3A%22GetCdnDispatch%22%2C%22param%22%3A%7B%22guid%22%3A%229756534816%22%2C%22calltype%22%3A0%2C%22userip%22%3A%22%22%7D%7D%2C%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%226541487400%22%2C%22songmid%22%3A%5B%22"+song_mid+"%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%220%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A0%2C%22format%22%3A%22json%22%2C%22ct%22%3A20%2C%22cv%22%3A0%7D%7D"
	return gethtml(vkeyurl,"")


def download_file(mp3_url,file_folder,filename):
	#文件夹不存在创建文件夹
	path="D:\\Python\\QQmusic\\"+file_folder
	folder=os.path.exists(path)
	file=path+"\\"+filename
	if not folder:
		os.makedirs(path)
	else:
		if os.path.exists(file):
			return
	try:
		print("下载文件："+filename)
		request.urlretrieve(mp3_url, path+"\\"+filename)
	except Exception:
		print("获取文件异常："+filename)

#获取QQ音乐网络热歌
url="https://u.y.qq.com/cgi-bin/musicu.fcg?-=getradiosonglist4871281737878832&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22songlist%22%3A%7B%22module%22%3A%22pf.radiosvr%22%2C%22method%22%3A%22GetRadiosonglist%22%2C%22param%22%3A%7B%22id%22%3A199%2C%22firstplay%22%3A1%2C%22num%22%3A10%7D%7D%2C%22radiolist%22%3A%7B%22module%22%3A%22pf.radiosvr%22%2C%22method%22%3A%22GetRadiolist%22%2C%22param%22%3A%7B%22ct%22%3A%2224%22%7D%7D%2C%22comm%22%3A%7B%22ct%22%3A%2224%22%7D%7D"
html=gethtml(url,"")
jsonhtml=json.loads(html)
songlist=jsonhtml["songlist"]["data"]["track_list"]
for song in songlist:
	try:
		title=song["title"]
		songvkey=getdownurl(song["mid"])
		jsonsong=json.loads(songvkey)
		ips=jsonsong["req"]["data"]["freeflowsip"]
		for ip in ips:
			songurl=ip+jsonsong["req_0"]["data"]["midurlinfo"][0]["purl"]
			download_file(songurl,"网络热歌",title+".mp3")
	except Exception as e:
		print("歌曲："+title+"下载失败")
