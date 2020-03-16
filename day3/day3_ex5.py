
class A(object):
    def __init__(self):
        self.num1 = 100
        self.__num2 = 521

    def test1(self):
        print("公有方法...")

    def __test2(self):
        print("私有方法...")

    def test3(self):
        print("...公有方法中调用私有属性和私有方法")
        self.__test2()
        print(self.__num2)
        print(self.num1)

class B(A):
    def test4(self):
        self.test3()

b = B()
b.test4()