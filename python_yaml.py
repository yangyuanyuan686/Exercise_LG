import yaml

# yaml 文件的创建

data = {"a": 123, "b": 456, "c": [1, 2, 3]}

# yaml文件的写入：dump将python格式的对象写入到yaml文件中
with open('data.yaml', "w") as f:
    yaml.dump(data, f)

# yaml文件的读取：safe_load 从yaml文件中读取数据，并输出为python的对象
with open('data.yaml', "r") as f:
    print(yaml.safe_load(f))

with open('data.yaml', "a+") as ff:
    yaml.dump(data={"e": [789]}, stream=ff)