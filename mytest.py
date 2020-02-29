'''
a = 3
b = 3.25
c = "Hello World!"
print(a,b,c)

name,age = input("请输入你的姓名及年龄，用逗号隔开：").split(',')
print(name,age)

# 一般的字符串打印
print("a、b、c的值为：",a,b,c)
# 使用格式化字符串
print('%d %f %s' % (a,b,c))
# 使用format格式化字符串
print("a={},b={},c={}".format(a,b,c)
'''
alist = [4,9,3,1,5,6,7,8,2]
# print(alist[-3])
# print(alist[4::2])
# print(tuple(range(1000)))
b = [2,3]
alist.insert(3,11)
alist.append(5)
# alist.pop(5)
alist.remove(5)
print(alist)
print(alist.index(4))
print(alist.count(5))
print(len(alist))
print(2 in alist)
print(max(alist))
print(min(alist))
print(alist.clear())

a = 2
a *=6+3
print(a)



