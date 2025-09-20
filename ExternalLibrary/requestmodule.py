import requests

# url="https://www.udemy.com/course/codewithharry-python/learn/lecture/52002793?start=0#reviews"

# response=requests.get(url)
# print(response.text)

url="https://jsonplaceholder.typicode.com/posts"


data={
    "title": 'jagannath',
    "body": 'Nahak',
    "userId": 1,
  }
headers={
    'Content-type': 'application/json; charset=UTF-8',
  }
response=requests.post(url,headers=headers,json=data)

print(response.text)
