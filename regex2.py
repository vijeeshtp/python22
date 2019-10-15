import requests as req

import re

res= req.get("http://www.expertzlab.com/contact.php")
res= re.findall("[0-9]{2}-[0-9]{10}", res.text)

for x in res:
    print (x)


