import requests

#  post requests sends data in a reqeust body not hte url
url_post = "https://httpbin.org/post"
payload = {"name":"Muzammil","ID":"123"}
r_post = requests.post(url_post, data=payload)
print("POST request url: ",r_post.url)
#  post requests has no name or valuepairs in its url like get

print(r_post.request.body)
# post request has a body while get does not
#  and this is in a json type so format it in that
#  then the key form will have our payload data

print(r_post.json()['form'])

# {'ID': '123', 'name': 'Muzammil'}