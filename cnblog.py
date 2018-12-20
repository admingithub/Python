from bs4 import BeautifulSoup
from urllib import request

url="https://www.cnblogs.com/" 
response=request.urlopen(url)
html=response.read();
html=html.decode("utf-8")
bs=BeautifulSoup(html,"html.parser")
#print(bs)
# post_list=[]
# for data in bs.find_all('h3'):
# 	print("标题："+data.text)
# post_list_item=[]
# for data in bs.find_all("p",class_='post_item_summary'):
# 	print("内容："+data.text)
for item in bs.find_all("div",class_="post_item"):
	title=item.find('h3').text.strip()
	tuijian=item.find("div",class_="diggit").text.strip()
	touxiang="暂无"
	if item.find("img",class_="pfs") is not None:
		touxiang=item.find("img",class_="pfs").get('src').strip()
	data=item.find("p",class_='post_item_summary').text.strip()
	user=item.find("div",class_="post_item_foot").text.strip()
	#print(touxiang.get('src'))
	print("推荐："+tuijian+"\r\n头像Url："+touxiang+"\r\n标题："+title,"\r\n内容："+data,"\r\n用户："+user)
