def exercises():
    """列表[11,13,5,7,0,56,23,34,72]，
    求该列表中的最大值，最小值及列表中一共有几个元素
    获取56元素在列表的位置
    追加元素7
    删除元素0
    排序列表（由大到小）
    将列表[66,67,68]与原列表组合"""
    s = [11,13,5,7,0,56,23,34,72]
    print("列表s的最大值为{}，最小值为{}，列表中共有{}个元素".format(max(s),min(s),len(s)))
    # 获取56元素在列表的位置
    print(s.index(56))
    # 向列表s中追加元素7
    s.append(7)
    print(s)
    # 删除元素0
    del s[s.index(0)]
    # 排序列表（由大到小）
    s.sort()
    s.reverse()
    print(s)
    # 将列表[66,67,68]与原列表组合
    s1 = [66,67,68]
    s.extend(s1)
    print(s)
# 预习后编程练习作业
# 1、求10阶乘
# 2、求100以内能被3整除的数，并将作为列表输出
# 3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
# 4、求斐波那契数列 1 2 3 5 8 13 ……
# 5、求10000以内的质数

def assignment_1(n=10):
    result = 1
    """求10阶乘"""
    while true:
        if n>=1:
            result *= n
            n -= 1
        else:
            break
    return result

def assignment_2(n=100):
    """求100以内能被3整除的数，并将作为列表输出"""
    result = []
    for num in range(1,n):
        if num % 3 ==0:
            result.append(num)
    # 或者使用列表推导式
    # result = [num for num in range(1,n) if num % 3 == 0]
    return result

def assignment_3():
    """列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表"""
    a = [1,2,3,4,3,4,2,5,5,8,9,7]
    re = set(a)
    return list(re)

def assignment_4():
    """求斐波那契数列 1 2 3 5 8 13 ……"""
    alist = [1,2]
    print(alist[0])
    print(alist[1])
    while True:
        result = alist[-1]+alist[-2]
        alist.append(result)
        print(result)
        if result >100:
            break


def assignment_5(n=10000):
    """求10000以内的质数"""
    result = []
    for num in range(2,n):
        for i in range(2,num):
            if num % i ==0:
                break
        else:
            result.append(num)
    return result

def main():
    print(assignment_4())

if __name__=="__main__":
    main()

