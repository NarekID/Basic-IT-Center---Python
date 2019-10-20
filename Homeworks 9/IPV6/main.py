import re

s = "abcd::A45a::gr41::1024"
s2 = "abcd::aa::gr41::1024"
s3 = "0bcd::z4aa::gr41::1024"
s4 = "ab43:az40::34zh:hkya"
pattern = "^[a-zA-Z1-9]{1}\w{3}::" \
          "[a-zA-Z1-9]{1}\w{3}::" \
          "[a-zA-Z1-9]{1}\w{3}::" \
          "[a-zA-Z1-9]{1}\w{3}"

res = re.findall(pattern, s)
print(res)
res = re.findall(pattern, s2)
print(res)
res = re.findall(pattern, s3)
print(res)
res = re.findall(pattern, s4)
print(res)