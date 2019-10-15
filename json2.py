import json



with open ("myjson.txt.py") as f:
    d = json.load(f)
    print (d['name'])

d['mark'] = 44
d['name']=  d['name'].upper()

with open ("myjson1.txt", "w") as f:
    json.dump(d,f)


