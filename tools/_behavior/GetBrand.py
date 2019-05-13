# coding:utf-8

import sys
sys.path.append('../')

from _imports import *
from _conf    import app_agent , app_config


# get all Brand Data By Loop Category
ListJSON = {"CategoryIdList":[1470,2619,2883,6781,20491,17588,9693,3667,2892,2722,2885]};
CategoryIdList =  ListJSON["CategoryIdList"]

print(CategoryIdList)


# CategoryURL
# url = app_config.CategoryURL
url = "https://search.kaola.com/category/1470.html"



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
resAll = "".join(re.findall(r"brandList=(.+?);",res))



f = open('../_data/BrandList.json', 'w', encoding='utf-8', errors='ignore')
f.write(resAll)
f.close()
























# data = demjson.decode(res)
# frontCategoryList = data['body']['frontCategoryList']
# categoryIdList = []


# for item in frontCategoryList: 
#   categoryIdList.append(item['categoryId'])


# dictId = demjson.encode({ "CategoryIdList": categoryIdList})


# f = open('../_data/CategoryIdList.json', 'w', encoding='utf-8', errors='ignore')
# f.write(dictId)
# f.close()