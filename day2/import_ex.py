# import Mymodule
# from Mymodule import *
# print(add(3,4))

from MyPythonLib import Mymodule2

print(Mymodule2.div(3,4))

if __name__ == '__main__':
    print(__file__.__doc__)