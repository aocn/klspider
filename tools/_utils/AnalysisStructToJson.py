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
		currency  		= it(".cur").text()[0:1]
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


