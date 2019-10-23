import requests
from time import sleep as slp

d = {}
d["name"] = "Narek"

res = requests.request("GET", "https://httpbin.org/image/jpeg")
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("GET", "https://httpbin.org/cookies/set")
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("GET", "https://httpbin.org/links/5/2")
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("GET", "https://httpbin.org/cache/5")
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("GET", "https://httpbin.org/status/200")
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("POST", "https://httpbin.org/status/201", data=d)
print(res.status_code)
print(res.content)
slp(2)

d = "some data"
res = requests.request("POST", "https://httpbin.org/response-headers", data=d)
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("POST", "https://httpbin.org/anything/any123", data=d)
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("POST", "https://httpbin.org/anything/any123", data=d)
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("POST", "https://httpbin.org/delay/5", data=d)
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("PUT", "https://httpbin.org/anything", data=d)
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("PUT", "https://httpbin.org/anything/anydata", data=d)
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("PUT", "https://httpbin.org/put", data=d)
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("PUT", "https://httpbin.org/status/200", data=d)
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("PUT", "https://httpbin.org/delay/6", data=d)
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("DELETE", "https://httpbin.org/delete", data=d)
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("DELETE", "https://httpbin.org/status/200", data=d)
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("DELETE", "https://httpbin.org/delay/2", data=d)
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("DELETE", "https://httpbin.org/delay/2", data=d)
print(res.status_code)
print(res.content)
slp(2)

res = requests.request("DELETE", "https://httpbin.org/anything", data=d)
print(res.status_code)
print(res.content)
# slp(2)