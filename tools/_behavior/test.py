

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
  # temp = demjson.decode( f.read() )


str2 = "\u8d44\u751f\u5802".encode('utf-8')
print (str2)

# print(isinstance(temp[0]["BrandList"][0], 'unicode'))
# print(temp[0]["BrandList"][0])

open('./test.json', 'w', encoding='utf-8', errors='ignore')
f.write(str2)
f.close()
