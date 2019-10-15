import re

mytext = "My name is Tom ,Phone My  Office Phone number \\n is [9988554455]." \
         "I have a another Phone number 0123456789123 thanks." \
         "My offie email is vijeesh.tp@experzlab.com and my personal email is " \
         "vijtp@gmail.com"

#res = re.finditer( r"[a-z0-9._]{3,50}@[a-z0-9._]{4,50}", mytext)

#res=re.search("number", mytext)
#res = re.findall("number", mytext)
#res =re.match("My", mytext)

pattern= re.compile("Phone")
res= pattern.sub("Mobile", mytext)
print (res)


