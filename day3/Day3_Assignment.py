# 1、打印小猫爱吃鱼，小猫要喝水

class Cat(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food,water):
        print("{0}爱吃{1}, {0}要喝{2}".format(self.name,food,water))

def main_ex1():
    cat = Cat("小猫")
    cat.eat('鱼','水')

"""
2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤
"""
class Person(object):
    def __init__(self,name,wg):
        self.name = name
        self.wg = wg

    def weight(self):
        print("{0}的体重是{1}公斤".format(self.name,self.wg))

class PerXM(Person):
    def __init__(self,name,wg):
        Person.__init__(self,name,wg)

    def interest(self):
        print("{0}爱跑步，爱吃东西。".format(self.name))

    def eat(self):
        self.weight()
        self.wg += 1
        print("每次吃东西体重会增加1公斤,体重变为：",self.wg)

    def run(self):
        self.weight()
        self.wg -= 0.5
        print("每次跑步会减肥0.5公斤,体重变为：",self.wg)

def main_ex2():
    xiaoming = PerXM("小明",75.0)
    xiaoming.eat()
    xiaoming.run()
    # 小美的体重是45.0公斤
    xiaom = Person("小美", '45.0')
    xiaom.weight()

"""
3、摆放家具
需求：
1）.房子有户型，总面积和家具名称列表
   新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平面
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
"""
""""
分析：类--房子，方法--添加，属性--总面积、户型、床、衣柜、餐桌
"""
class House(object):
    def __init__(self,area,houseType):
        self.area = area
        self.houseType = houseType
        self.bed = 4
        self.closet = 2
        self.diningTable = 1.5

    def add(self):
        room = int(self.houseType[0])
        hall = int(self.houseType[2])
        reArea = self.area-(self.bed+self.closet)*room-self.diningTable*hall
        return room,hall,reArea

    def print_re(self):
        rooms,halls,re = self.add()
        print("房子户型{0}，总面积{1}，剩余面积{2}，摆放{3}张床，{3}个衣柜，{4}个餐桌。".\
              format(self.houseType,self.area,re,rooms,rooms,halls))

def main_ex3():
    house = House(50,'3室1厅')
    house.print_re()

"""
4.士兵开枪
需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量
"""
"""
分析：类-士兵、枪，属性--姓名、子弹，方法开火，发射，装填
"""
class Gun(object):
    def __init__(self,bullet):
        self.bullet = bullet

    def shoot(self):
        print(self.bullet.name)
        pass

    def chargeFull(self):
        pass

class soldier(object):
    def __init__(self,name):
        self.name = name




def main_ex4():
    sd = soldier("瑞恩")
    gun = Gun(sd)
    gun.shoot()


if __name__ == '__main__':
    main_ex4()

