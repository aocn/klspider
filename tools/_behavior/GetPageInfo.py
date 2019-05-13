# coding:utf-8

import sys
sys.path.append('../')
from _imports import *
from _utils.AnalysisPageNumber import getTotalPageNumber


# Get URLS
# Get all Brand Data By Loop Category
temp = ''
with codecs.open("../_data/allBrandURLs.json", 'r', 'utf-8') as f:
  temp = json.loads(f.read())


listLen = len(temp)

for item in temp:
	categoryId = item["CategoryId"]
	urlLists = item["BrandList"]
	for url in urlLists:
		# get all info



print( len(temp[1]["2619"]) )



#Get urls
# print(temp[0]["1470"])

# print(temp[0]["1470"])

# print(len(temp))

# thisUrl = temp[0]["1470"][1]

# maxPage = getTotalPageNumber(thisUrl)

# print(maxPage)

















