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

if __name__ == '__main__':
    # getPrimeNumber()
    filename = 'input2.txt'
    # day2_ex4(filename)
    day2_ex1()