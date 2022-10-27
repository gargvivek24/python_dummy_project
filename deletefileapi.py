import requests
from requests.auth import HTTPBasicAuth

abc = requests.get(
  'https://test.singlerulebook.com/login',
  auth=HTTPBasicAuth('isha.taneja@singlerulebook.com', 'fXkEVua/0aRfvu')
)
print(abc.text)



x = requests.delete('https://test.singlerulebook.com/srb/recent/labels')

print(x)


print(x.status_code)

print(x.text)

url = 'https://test.singlerulebook.com/srb/regs/eu/aifmd/recital-1-of-aifmd'

response = requests.get(url)

# <Response [200]>
print(response)

# 200
print(response.status_code)
print(response.text)