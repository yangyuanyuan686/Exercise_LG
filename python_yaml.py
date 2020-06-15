import yaml

# yaml 文件的创建


data = {"a": 123, "b": 456, "c": [1, 2, 3]}

# yaml 文件的写入将python格式的对象下入到yaml文件中
with open('data.yaml', "w") as f:
    yaml.dump(data, f)

# yaml 文件的读取：从yaml文件中读取数据，并输出为python的对象
with open('data.yaml', "r") as f:
    print(yaml.safe_load(f))

with open('data.yaml', "a+") as ff:
    yaml.dump(data={"e": [789]}, stream=ff)