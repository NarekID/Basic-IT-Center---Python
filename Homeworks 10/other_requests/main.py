import requests
from time import sleep as slp

d = {"name": "Narek"}

# HTTP MEthods
slp(2)
res = requests.request("DELETE", "https://httpbin.org/delete", data=d)
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/get")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("POST", "https://httpbin.org/post", data=d)
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("PUT", "https://httpbin.org/put", data=d)
print(res.status_code)
print(res.content)

# Auth methods
slp(2)
res = requests.request("GET", "https://httpbin.org/basic-auth/user123/pass123")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/bearer")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/digest-auth/auth/mylogin/mypass")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/digest-auth/auth/mylogin/mypass/md5/")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/digest-auth/auth/mylogin/mypass/md5/never")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/hidden-basic-auth/mylogin/mypass/")
print(res.status_code)
print(res.content)

# Status codes
slp(2)
res = requests.request("DELETE", "https://httpbin.org/status/201", data=d)
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/status/401")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("POST", "https://httpbin.org/status/200", data=d)
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("PUT", "https://httpbin.org/status/401", data=d)
print(res.status_code)
print(res.content)

# Request inspection
slp(2)
res = requests.request("GET", "https://httpbin.org/headers")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/ip")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/user-agent")
print(res.status_code)
print(res.content)

# Response inspection
slp(2)
res = requests.request("GET", "https://httpbin.org/cache")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/cache/1024")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/response-headers/")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("POST", "https://httpbin.org/response-headers/", data=d)
print(res.status_code)
print(res.content)

# Dynamic data
slp(2)
res = requests.request("GET", "https://httpbin.org/base64/useRJGIjafRJGe")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/bytes/512")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("DELETE", "https://httpbin.org/delay/3", data=d)
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/drip")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/links/8/3")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/range/8")
print(res.status_code)
print(res.content)

# Cookies
slp(2)
res = requests.request("GET", "https://httpbin.org/cookies/delete")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/cookies/set/namecookie/1024")
print(res.status_code)
print(res.content)

# Images
slp(2)
res = requests.request("GET", "https://httpbin.org/image")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/image/jpeg")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/image/png")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/image/svg")
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("GET", "https://httpbin.org/image/webp")
print(res.status_code)
print(res.content)

# Anything
slp(2)
res = requests.request("DELETE", "https://httpbin.org/anything", data=d)
print(res.status_code)
print(res.content)

slp(2)
res = requests.request("PUT", "https://httpbin.org/anything/any123", data=d)
print(res.status_code)
print(res.content)