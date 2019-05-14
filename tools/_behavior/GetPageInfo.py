# coding:utf-8

import sys
sys.path.append('../')
from _imports import *
# from _utils.AnalysisPageNumber import getTotalPageNumber
from _utils.GetGoodsInfo import getAllPageInfo


# Get URLS
# Get all Brand Data By Loop Category
temp = ''
with codecs.open("../_data/allBrandURLs.json", 'r', 'utf-8') as f:
  temp = json.loads(f.read())


tmp = [{
		"BrandList": [
				"https://search.kaola.com/category/2885.html?&b=9641",
				# "https://search.kaola.com/category/2885.html?&b=15600",
				"https://search.kaola.com/category/2885.html?&b=9964"
			],
		"CategoryId":"2885"
	}]


def getBrandId(url):
	return str(12345)

def getBrandName(id):
	return "喜之郎"


for item in tmp:
	categoryId = item["CategoryId"]
	urlLists = item["BrandList"]
	for url in urlLists:
		brandId = getBrandId(url)
		brandName = getBrandName(brandId)

		resData = getAllPageInfo(url, brandId, brandName)
		f = open('../_data/FinalGoodsData/'+ str(categoryId) +'.json', 'a+', encoding='utf-8', errors='ignore')
		f.write(demjson.encode(resData))
		f.close()


