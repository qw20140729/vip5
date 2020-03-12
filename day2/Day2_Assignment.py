# -*- encoding:utf-8 -*-
from datetime import datetime
# 求斐波那契数列 1 1 2 3 5 8 13 ……
def day2_ex1():
    alist = [1,1]
    n = int(input("请输入一个大于2的正整数，返回一个裴波那契数列："))
    for i in range(n):
        if i<2:
            pass
        else:
            re = alist[i-2]+alist[i-1]
            alist.append(re)
    print(alist)

# 求100以内的质数（只能被1和它本身整除）
def getPrimeNumber(n=100):
    primeList = []
    for num in range(2,n):
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            primeList.append(num)
    print(primeList)

# 读取以下文件的全部内容，并将所有的数字去重后，放入一个列表
"""
11,10,18
2,23,24
22,1,0
13,7
5
29,19
10,1,3,5,9
"""
def day2_ex3(filename):
    resultlist = []
    with open(filename,'r') as f:
        for line in f.readlines():
            newlist = line.strip().split(',')
            for num in newlist:
                if int(num) not in resultlist:
                    resultlist.append(int(num))
    print(resultlist)

"""
11,10,18
2,23,24
22,1,0
13,7
5
29,19
10,1,3,5,9
"""
# 将以上文件的全部内容写入一个新的文件，并按照从小到大的顺序
def day2_ex4(filename):
    resultlist = []
    with open(filename,'r') as f:
        for line in f.readlines():
            newlist = line.strip().split(',')
            resultlist.extend(newlist)
    re = [int(i) for i in resultlist]
    re.sort()
    with open('output.txt','w') as nf:
        for i in re:
            nf.write(str(i)+'\t')

def getPersonInfo(filename):
    perdict = dict()
    f = open(filename,'r',encoding='UTF-8')
    for line in f:
        re = line.strip().split('|')
        perdict[re[0]] = re
    f.close()
    return perdict
def day2_ex4():
    """
    任务1-找出所有L开头的人名
    任务2-按照年龄进行排序
    任务3-找出所有女性用户的信息
    """
    filename = 'PersonInfo.txt'
    person = getPersonInfo(filename)
    print(person)
    # 找出所有L开头的人名
    for per in person.keys():
        if per.startswith('L'):
            print("以L开头的人：",per)
    # 按照年龄进行排序
    perlist = []
    for per in person.keys():
        age = datetime.now().year - int(person[per][3][:4])
        perlist.append(age)
    print(perlist)
    # 找出所有女性用户的信息
    for per in person.keys():
        if person[per][2]=='女':
            print("性别为女的人员：",per)


if __name__ == '__main__':
    # getPrimeNumber()
    filename = 'input2.txt'
    # day2_ex4(filename)
    day2_ex4()