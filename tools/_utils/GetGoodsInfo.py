# coding:utf-8


import sys
sys.path.append('../')
from _imports import *
from _conf    import app_agent , app_config

from  . import AnalysisPageNumber
import string

def getOnepageData(baseurl):
	reqM = request.Request(baseurl)

	user_agent, proxies=  app_agent.user_agent, app_agent.proxies

	# send request 
	proxy_support = urllib.request.ProxyHandler({'http':random.choice(proxies)})
	opener = request.build_opener(proxy_support)
	request.install_opener(opener)


	# get request
	result = request.urlopen(reqM)
	html=result.read()
	html=html.decode('utf-8')


	# analysis html tags
	htmlText = etree.HTML(html)

	p = pq(htmlText);
	pResult = p('#result').html()  
	# p = pq(html3).text();


	# all tages and loop items
	doc = pq(pResult)
	its = doc("li").items()

	# TODO: 将 html-struct 解析成对应格式的 json
	resu =''
	for it in its:
	    # print(it.text())

	    resu += it.text()+"\r\n\r\n"
	    # resu += it.html()+"\r\n\r\n"

	# f = open('./adminABC.txt', 'w+', encoding='utf-8', errors='ignore')
	# f.write(resu)
	# f.close()

	return resu;


def getAllPageInfo(url):
	num = AnalysisPageNumber.getTotalPageNumber(url)
	data = '';
	for i in (1, num+1):
		# url = url+"&pageNo="+str(i)
		url = url+"&pageNo="+ '2'

		data += (getOnepageData(url))
		time.sleep( 1 )
		print('wait 1s...')

	return data



# getOnepageData("https://search.kaola.com/category/1470.html?&b=1200")
# getAllPageInfo("https://search.kaola.com/category/1470.html?&b=1200")


