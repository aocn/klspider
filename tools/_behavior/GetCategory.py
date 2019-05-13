# coding:utf-8

import sys
sys.path.append('../')

from _imports import *
from _conf    import app_agent , app_config


# CategoryURL
url = app_config.CategoryURL


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


data = demjson.decode(res)
frontCategoryList = data['body']['frontCategoryList']
categoryIdList = []


for item in frontCategoryList: 
  categoryIdList.append(item['categoryId'])


dictId = demjson.encode({ "CategoryIdList": categoryIdList})


f = open('../_data/CategoryIdList.json', 'w', encoding='utf-8', errors='ignore')
f.write(dictId)
f.close()
