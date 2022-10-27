url="http://ip.jsontest.com/"
import requests


response = requests.get(url=url)
payload= {"key1":"value1","key2":"value2”"}
response_post=requests.post(url=url,json=payload)
print(response_post)
response_json=response_post.json()
print(response_json)
print(response)
response_json1 = response.json()
print(response_json1)
