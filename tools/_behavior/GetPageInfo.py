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


# tempReflect = ''
# with codecs.open("../_data/CategoryBrandData/BrandReflectName.json", 'r', 'utf-8') as f:
#   tempReflect = json.loads(f.read())

def getBrandIdName(url):
	brandTag = url.split("&b=")[1].split("&namebrand=")
	return brandTag[0], brandTag[1]

for item in temp:
	categoryId = item["CategoryId"]
	urlLists = item["BrandList"]
	for url in urlLists:
		brandId, brandName = getBrandIdName(url)
		url = url.split("&namebrand")[0]
		resData = getAllPageInfo(url, brandId, brandName)
		f = open('../_data/FinalGoodsData/'+ str(categoryId) +'.json', 'a+', encoding='utf-8', errors='ignore')
		f.write(demjson.encode(resData))
		f.close()


