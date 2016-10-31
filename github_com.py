import sys
import demjson
import requests

q = sys.argv[1]
search_keyword = q.replace(' ','+')
sort = sys.argv[2]
order = sys.argv[3]

users500=[]

for rang in range(1,6):
    r = requests.get("https://api.github.com/search/repositories?q="+search_keyword+"&sort="+sort+"&order="+order+"&per_page=100&page="+str(rang))    
    data = r.text
    dct = demjson.decode(data)
    loop = dct['items']
    for each in loop:
        users500.append(each['owner']['login'])

for user in users500:
    print str(user)
