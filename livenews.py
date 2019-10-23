import requests as req
import xml.etree.ElementTree as et

data=req.get ("https://www.hindustantimes.com/rss/topnews/rssfeed.xml")

#print (data.text)

xmldata=et.fromstring(data.text)
#print (xmldata)
for x in xmldata:
    for y in x.findall('item'):
        for z in y.findall('title'):
            print (z.text)


