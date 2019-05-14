# coding:utf-8


import sys
sys.path.append('../')

from _imports import *
from _conf    import app_agent , app_config


temps = []
with codecs.open("../_data/CategoryBrandData/BrandIdReflectName.json", 'r', 'utf-8') as f:
	temps.append(json.loads(f.read()))


def getReflect(tmp, key):
	key = str(key)
	for item in tmp:
		if item[key] is not None:
			return item[key]



rs = getReflect( temps, "2656")

f = open('./aaaaT.json', 'w+', encoding='utf-8', errors='ignore')
f.write( rs )
f.close()
