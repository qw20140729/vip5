# set1 = {1,5,7,89,8}
# dict1 = {'a':2,'b':23,'c':'name'}
# # 为集合和字典分别插入元素55，（d：55）
# set1.add(55)
# dict1['d'] = 55
# # 分别删除集合和字典中一个元素
# set1.remove(5)
# del dict1['a']
# # 取出字典内的所有值和 集合组合成一个列表
# newList = list(dict1.values())
# newList.extend(list(set1))
# print(newList)
# # 集合和字典的区别：
# """
# 相同点
# 1、集合和字典都是无序的
# 2、集合和字典不能通过下标访问
# 不同点
# 集合中的元素是一个值，字典中的每个元素是键-值对；
# """

# num = int(input("请输入一个数字："))
# list1 = [2,3,45,6]
# if num in list1:
#     print("Happy")
#     index = list1.index(num)
#     list1[index] += 1
#     print(list1)
# else:
#     print("sad")
#
# grade = int(input("请输入一个数字："))
# if 90<=grade<=100:
#     print("A")
# elif 80<=grade<90:
#     print("B")
# elif 70<=grade<80:
#     print("C")
# elif 60<=grade<70:
#     print("D")
# elif grade<60:
#     print("E")

# # 1-循环变量
# n = 1
# result = 0
# # 2-循环条件
# while n<=100:
#     # 3-循环体
#     result += n
#     # 循环变量发生变化
#     n += 1
# print(result)
# 求10的阶乘
# sum = 1
# for i in range(1,10+1):
#     sum *= i
# print(sum)
# # 求100以内能被3整除的数，并作为列表输出
# re = []
# for num in range(1,101):
#     if num % 3 ==0:
#         re.append(num)
# print(re)
# # 列表[1,2,3，4,3,4,2,5,5,8,9,7]，将此列表去重，得到一个唯一元素的列表
# a = [1,2,3,4,3,4,2,5,5,8,9,7]
# set1 = set()
# for j in a:
#     set1.add(j)
# b = list(set1)
# print(b)

# example4 = [[1,2,3],[4,5,6],[7,8,9],[10]]
# exmaple5 = [j**2 for i in example4 if len(i)>1 for j in i if j%2 == 0]
# listre = []
# for i in example4:
#     if len(i) > 1:
#         for j in i:
#             if j%2 ==0:
#                 listre.append(j**2)
#
# print(listre)
# print(exmaple5)

# def calculate(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
# x,y = input("请输入两个数，用逗号隔开：").split(',')
# calculate(int(x),int(y))
#
# def calculate2(a,b,c):
#     if c == '+':
#         return a+b
#     elif c == '-':
#         return a-b
#     elif c == '*':
#         return a*b
#     elif c == '/':
#         return a/b
# m,n = input("请输入两个数，用逗号隔开：").split(',')
# f = input("请输入您要计算的运行符加+ 减- 乘* 除/：")
# print(calculate2(int(m),int(n),f))

# def calc(a,b):
#     try:
#         print(a/b)
#         # print(num)
#     except (BaseException,Exception) as msg:
#         print('除数不能为了0')
#         print(msg)
#     else:
#         print("程序正常执行...")
#     finally:
#         print("程序执行结束...")
# calc(30,0)
# 读取全部内容
with open('input.txt','r') as f:
    print(f.read())
print("-- "*20)
# 读取每一行的内容
with open('input.txt','r') as f:
    print(f.readline())
print("-- "*20)
# 读取所有行的内容
with open('input.txt','r') as f:
    print(f.readlines())
print("-------第2题---------")
# 读取文件的全部内容，并将所有的数字去重后，放入列表
reList = []
with open('input2.txt','r') as nf:
    for line in nf.readlines():
        newlist = line.strip().split(',')
        for j in newlist:
            if int(j) not in reList:
                reList.append(int(j))
print(reList)
print("----------第3题-----------")
with open('outputdata.txt','w') as nf:
    reList.sort()
    for i in reList:
        nf.write(str(i)+'\n')
