from fra import *
import os
num = 1
per_list = ""
url = "https://www.fragrancenet.com/fragrances?f=0!4V&page="
result = getNAList(url+str(num))

while( len(result)>0):
    string   = "\n".join(x for x in result)
    per_list += (string)
    num      += 1
    result = getNAList(url + str(num))
now  = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
path = os.path.join("NAlist",now)
writeToFile(per_list,path)
