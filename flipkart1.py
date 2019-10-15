import requests
import json

res =requests.get("https://www.flipkart.com/lc/getData?dataSourceId=websiteNavigationMenuDS_1.0&t=26183917")

#print (res.text)

d = json.loads(res.text)

for k,v in d ["navData"].items ():
    print (k , v ['title'])


