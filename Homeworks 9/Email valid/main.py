import re

mail = "example@gmail.com"

pattern = "^\w{1}[a-zA-Z0-9_\-.,*]{3,}@\w+\.[ru|com|ai|net|io]+$"

res = re.findall(pattern, mail)
print(res)
