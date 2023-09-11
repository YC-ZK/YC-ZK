# import mysql.connector;
print("Hello, World!")
print("-----------------------------------------------")
name = int(input("请输入你的预期价格:"))
print("你输入的价格是:",name)
if name > 1000:
    print("太贵了")
else:
    print("价格在预期内")

name = "YC"
age = 22
# %s 占位
# %d 占位
#s = "我叫%s,我今年%d岁" % (name,age)
#f-string
s = f"我叫{name},我今年{age+1}岁"
print(s);
# i = 10;
# print(type(i))
