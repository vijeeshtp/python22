import json

x =  '{ "name":"Ramu", "phone":"787878898"}'
d = json.loads(x)
print (d['name'])

d['mark'] = 44
d['name']=  d['name'].upper()

s=json.dumps(d)
print (s)




