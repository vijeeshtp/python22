import xml.etree.ElementTree as et

data = et.parse("xmldata.xml")


print (data.getroot())



for x in data.getroot():
    print (x.tag, x.attrib)
    for y in x :
        print ("    ",y.tag, y.attrib)

        for z in y:
            print("         ", z.tag, z.attrib)