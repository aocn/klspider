# coding:utf-8

# method for request by url
# -------------------------------------------------------


# request
import urllib
from urllib import request

#
import random
import chardet



# url
url = "https://search.kaola.com/category/1470.html"

# CONFIG  ???? get proxies , .... from  _config

# send request 
proxy_support = urllib.request.ProxyHandler({'http':random.choice(proxies)})
opener = request.build_opener(proxy_support)
request.install_opener(opener)


# get request
result = request.urlopen(reqM)
rs=result.read()
res=rs.decode('utf-8')


#  return  res  out 
