friend={"first_name":"小颖","last_name":"陈","age":25,
        "city":"深圳"}
print("姓名："+friend["last_name"]+friend["first_name"])
print("年龄:"+str(friend["age"]))
print("城市:"+friend["city"])


rivers={"Nile":"Egypt","Yangtze River":"China","Amazon River":"Brazil"}
for river,county in rivers.items(): #.items()键和对应的值成对取出
    print("The "+river+" run through "+county+".")
for river in rivers.keys():
    print(river)
for county in rivers.values():
    print(county)


gpa_dic={"小明":3.251,"小花":3.869,"小李":2.683,"小张":3.685}
for name,gpa in gpa_dic.items():
    print("{0}你好，你的当前绩点为：{1:.2f}".format(name,gpa))


gpa_dic={"小明":3.251,"小花":3.869,"小李":2.683,"小张":3.685}
for name,gpa in gpa_dic.items():
    print(f"{name}你好，你的当前绩点为：{gpa:.1f}")