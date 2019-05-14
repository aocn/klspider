# coding:utf-8


import sys
sys.path.append('../')
from _imports import *
from _conf    import app_agent , app_config

# GET SINGLE PAGE BY URL
import string


def structToJson(html, brandId, brandName):

	doc  = pq(html)
	p_ul = doc("#result")
	its  = p_ul(".goods").items()

	for it in its:
		brandId   		= brandId
		brandName 		= brandName
		goodsName 		= it(".title").text()
		currency  		= it(".cur").text()
		image 	  		= it(".imgtag").attr("src")
		country   		= it(".proPlace").text()
		price	  		= it(".cur").text().lstrip("\u00a5")
		marketprice	  	= it(".marketprice").text().lstrip("\u00a5\n")

		data = {
			"brandId"  		: brandId, 
			"brandName"		: brandName,
			"goodsName"		: goodsName,
			"currency" 		: currency,
			"currentPrice"  : price,
			"marketprice"   : marketprice,
			"country"  		: country,
			"image"	   		: image
		}

		return data




# def storeData(data):
# 	f = open('./struct_T.json', 'w', encoding='utf-8', errors='ignore')
# 	f.write(data)
# 	f.close()

# structToJson(html, 1122, '耐克美国')

# {
# 	"brandId":1143,
# 	"brandName":"美赞臣",
# 	"title":"MeadJohnson 美赞臣 荷兰版 铂睿幼儿配方奶粉（12-36月龄，3段）850/罐 原装原罐荷兰进口",
# 	"currency":"¥",
# 	"price1":"204.25",
# 	"price2":"",
# 	"country":"美国"
# 	"image":"....."
# }

