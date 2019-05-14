# coding:utf-8

import sys
sys.path.append('../')
from _imports import *
from _conf    import app_agent , app_config

from  . import AnalysisPageNumber
import string

from . import AnalysisStructToJson 



def getOnepageData(baseurl, brandId, brandName):
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
	resu = AnalysisStructToJson.structToJson(htmlText, brandId, brandName)
	return resu;


def getAllPageInfo(url, brandId, brandName ):
	num = AnalysisPageNumber.getTotalPageNumber(url)
	data = [];
	# brandId, brandName = brandId, brandName
	for i in range(1, num+1):
		sendURL = url+"&pageNo="+str(i)
		getData = getOnepageData(sendURL, brandId, brandName)
		data.append( getData )
		time.sleep( 1 )
	return data


