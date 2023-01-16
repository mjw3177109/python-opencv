import re


compliex =re.compile(r"^[0-9a-zA-Z_-]{0,19}@[0-9a-zA-Z]{1,13}(\.[com,cn,net]+){0,4}$")
str="ssa_a-c@ss.net.cn2"
res= compliex.match(str)

exc=re.compile(r"^1[3-9]\d{9}$")
if res:
    print("2")
# print(res[0])