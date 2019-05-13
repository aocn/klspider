# coding:utf-8

import sys
sys.path.append('../')
from _imports import *
from _conf    import app_agent , app_config

# GET SINGLE PAGE BY URL
# url

def getTotalPageNumber(url):

	# CategoryURL
	# prepare request
	reqM = request.Request(url)

	# url-agent && proxy-ip-address
	user_agent, proxies =  app_agent.user_agent, app_agent.proxies

	# send request 
	proxy_support = urllib.request.ProxyHandler({'http':random.choice(proxies)})
	opener = request.build_opener(proxy_support)
	request.install_opener(opener)

	# get request
	result = request.urlopen(reqM)
	json=result.read()
	res=json.decode('utf-8')

	# get request
	result = request.urlopen(reqM)
	html=result.read()
	html=html.decode('utf-8')

	# analysis html tags
	htmlText = etree.HTML(html)

	p = pq(htmlText);
	pResult = p('.splitPages').html()  

	# all tages and loop items
	doc = pq(pResult)
	its = doc("a").items()


	resu =[]
	for it in its:
	    resu.append(it.text())

	# ['2', '3', '4', '5', '6', '7', '8', '11', '▒▒һҳ'] 倒数第二个是最大长度 哈哈哈哈！！
	return resu[-2]

