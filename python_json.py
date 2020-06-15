import json

##dump:把json串中的数据类型转换成字符串并存储在文件中
data = {'wumei': {"floor1": [['iPhone', 12300], ['Bike', 800], ['shirt', 300]]}}
with open("data.json", "w") as f:
    json.dump(data, f)

##load: 把文件打开，把里面的字符串转json串
with open("data.json", "r") as f:
    print(json.load(f))

##dumps:对python对象进行处理，将其转变为字符串

print(type(json.dumps(data)))  ##str
print(json.dumps(data))
print(type(data))  ## dict

## loads:对python对象进行处理，将字符串转变为字典

data_str = '{"wumei1": {"floor1":123}}'
print(type(json.loads(data_str, encoding="UTF-8")))  ##dict
print(json.loads(data_str))
