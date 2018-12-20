from urllib import request
import json

#---------获取网页源代码--------------
def getHtml(url):
	response=request.urlopen(url)
	html=response.read()
	html=html.decode("utf-8")
	return html

#---------下载图片--------------
def downImg(url,filename):
	path="D:\\Python\\img\\"+filename
	request.urlretrieve(url,path)

page=1
while page<10:
	url="https://tu.fengniao.com/ajax/ajaxTuPicList.php?page="+str(page)+"&tagsId=13&action=getPicLists"
	html=getHtml(url)
	data_json=json.loads(html)
	index=0
	for x in data_json["photos"]["photo"]:	
		downImg(x["src"],x["id"]+".jpg")
		print("页码"+str(page)+",索引："+str(index)+",地址："+x["src"])
		index=index+1
	page=page+1
