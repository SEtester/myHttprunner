import requests
import json

# 登录接口
url = "http://127.0.0.1:5000/api/login"

payload = json.dumps({
  "username": "xiaoming",
  "password": "123456"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# 查询接口

url = "http://127.0.0.1:5000/api/books/2"

payload={}
headers = {
  'token': 'h7Gk4YJcV6'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# 查询所有

url = "http://127.0.0.1:5000/api/books"

payload={}
headers = {
  'token': 'h7Gk4YJcV6'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# 新增

url = "http://127.0.0.1:5000/api/books"

payload = json.dumps({
  "title": "java高级",
  "author": "不知名作者",
  "publication_date": "2023-3-19",
  "version": 1
})
headers = {
  'token': 'h7Gk4YJcV6',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# 更新

url = "http://127.0.0.1:5000/api/books/1"

payload = json.dumps({
  "title": "Python编程：从入门到实践2",
  "author": "Eric Matthes",
  "publication_date": "2016-11-01",
  "version": 1
})
headers = {
  'Cookie': 'token=h7Gk4YJcV6',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

# 删除
import requests

url = "http://127.0.0.1:5000/api/books/4"

payload = ""
headers = {
  'Cookie': 'token=h7Gk4YJcV6; token=h7Gk4YJcV6'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
