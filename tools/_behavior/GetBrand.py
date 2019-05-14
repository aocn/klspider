# coding:utf-8

import sys
sys.path.append('../')

from _imports import *
from _conf    import app_agent , app_config


# get all Brand Data By Loop Category
temp = ''
with codecs.open("../_data/CategoryIdList.json", 'r', 'utf-8') as f:
  temp = json.loads(f.read())
CategoryIdList =  temp["CategoryIdList"]
 

def CrawCategoryBrandData(url, filename, categoryId):
	# prepare request
	reqM = request.Request(url)

	# url-agent && proxy-ip-address
	user_agent, proxies=  app_agent.user_agent, app_agent.proxies

	# send request 
	proxy_support = urllib.request.ProxyHandler({'http':random.choice(proxies)})
	opener = request.build_opener(proxy_support)
	request.install_opener(opener)

	# get request
	result = request.urlopen(reqM)
	json=result.read()
	res=json.decode('utf-8')


	# def a func and solve url
	doc = pq(res)
	res = doc.find("script").text();

	# Get lists From URL
	# resAll = "".join()
	resAll =demjson.decode( re.findall(r"brandList=(.+?);",res)[1] )


	# BrandList = []
	BrandListURLs = []
	BrandIdReflectList = []
	for item in resAll:
		brandId, brandName = item['brandId'], item["brandName"]

		# BrandList.append(item['brandId'])
		BrandListURLs.append( url + '?&b='+ str( brandId) +"&namebrand="+ str(brandName) );

	# 添加 urls
	f = open('../_data/CategoryBrandData/url-'+ filename, 'w', encoding='utf-8', errors='ignore')
	f.write(demjson.encode({'FromCategory': categoryId ,'BrandListURLs': BrandListURLs }) )
	f.close()




	# 生成 brandId : brandName




	return BrandListURLs



ListURL = []

for item in CategoryIdList:

	current_url = "https://search.kaola.com/category/"+str(item["CategoryId"])+".html"
	filename = str(item["CategoryId"]) +'-'+item["CategoryName"] +'.json'

	urls = CrawCategoryBrandData(current_url, filename , item["CategoryId"])


	writeDoc = { 
			"CategoryId": str(item["CategoryId"]), 
			"BrandList":urls, 
		} 

	f = open('../_data/CategoryBrandURL/'+filename, 'w', encoding='utf-8', errors='ignore')
	f.write( demjson.encode( 
		writeDoc
	) )
	f.close()

	ListURL.append(writeDoc)


f = open('../_data/allBrandURLs.json', 'w', encoding='utf-8', errors='ignore')
f.write( demjson.encode( ListURL) )
f.close()

