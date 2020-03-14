
# class Student(object):
#     name = '小明'
#     cours = '数学'
#     sno = 3
#     def study(self):
#         print(self.name+'学习'+self.cours+'课程' )
#
# s = Student()
# s.study()

# class Student(object):
#     sno = 3
#     def study(self,name,course):
#         print('学号为{0}的学生，学习{1}课程'.format(self.sno,course))
#
# s = Student()
# s.study('小明','英语')

# class Student(object):
#     def __init__(self,sno,course):
#         self.sno = sno
#         self.course = course
#
#     def study(self):
#         print('学号为{0}的学生，学习{1}课程'.format(self.sno,self.course))
#
# s = Student(12,'语文')
# s.study()

class Person(object):
    name = None
    def eat(self,food):
        print("名字是{0}，工号为{1}的老师，吃{2}饭".format(self.name,3,food))

    def sleep(self):
        print('睡觉')

class Teacher(Person):
    gh = None
    def teach(self,course):
        print("gh为{0}的老师，教{1}课".format(self.gh,course))

    def salaire(self,city,sal):
        print("gh为{0}老师，在{1}上班，一月工资{2}".format(self.gh,city,sal))

teacher = Teacher()
teacher.gh = 3
teacher.name = '王五'
teacher.teach('数学')
teacher.salaire('上海',5000)
teacher.eat('米')

