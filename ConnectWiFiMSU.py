import re,requests
rf = open('./data.txt', 'r',encoding='utf-8')
data = rf.read().split(',')

# http://10.99.92.1/logout

req = requests.post('http://10.99.92.1/webAuth/index.htm',headers={
    "Content-Type":"application/x-www-form-urlencoded"
},data={
    "une": data[0],
    "username": data[0],
    "pass_wd": data[1],
    "pass_word": data[1]
})

print(req.status_code)
print(req.url)
