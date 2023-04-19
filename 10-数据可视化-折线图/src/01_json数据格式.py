import json

# 将嵌套字典的列表转换为json
data=[{"name":"张大山","age":11},{"name":"王大锤","age":13},{"name":"赵小虎","age":16}]
# json_str=json.dumps(data)
json_str=json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将字典转换为json
d={"name":"周杰伦","addr":"台北"}
json_str=json.dumps(d,ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将json字符串转换回列表
s='[{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]'
l=json.loads(s)
print(type(l))
print(l)

# 将json转换回字典
s='{"name":"周杰伦","addr":"台北"}'
d=json.loads(s)
print(type(d))
print(d)