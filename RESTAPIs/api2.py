from urllib import request

request1 = request.Request('http://127.0.0.1:5000/')

try:
    response1 = request.urlopen(request1)
    print(response1.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())

