import requests

url ="https://youtube.com"

r = requests.get(url)
print(r.status_code)
# 200 will mean ok
header = r.headers
print(header)
# this returns the python dictionary of http response headers
print(header['date'])
print(header["Content-Type"])
# this key in the header indicates the type of data
print(r.encoding)
#  wwe can check the encoding like uft unicode etc
print(r.text[0:50])
#  this way we can also see the content html text in the body 
#  as this is string we can do multiple operations on it as well just liek strings




print(r.request.body)
#  for get request we get no body

# querry string this sends another request to the internwet url


url_get = "https://youtube.com/get"
payload = {"name":"Alam","ID":"123"}
r = requests.get(url_get, params=payload)
#  this basically what it simply does is send the request directly throught he url
# it would be something like this
# https://www.youtube.com/get?name=Alam&ID=123
print(r.url)
print(r.status_code)
print(r.text[0:50])
header = r.headers
print(header)
print(header['Content-Type'])
#  this will be a json file
#  we2 can format it using the method json
formater = r.json()
print(formater)
print(formater['args'])
#  this args wil  have the name and values for the querry string