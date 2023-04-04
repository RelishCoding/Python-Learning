# 使用import导入time模块使用sleep功能（函数）
# import time
# print("hello")
# time.sleep(5)
# print("world")

# 使用from导入time的sleep功能（函数）
# from time import sleep
# print("hello")
# sleep(5)
# print("world")

# 使用*导入time模块的全部功能
# from time import *
# print("hello")
# sleep(5)
# print("world")

# 使用as给特定功能起别名
# import time as t
# print("hello")
# t.sleep(5)
# print("world")
from time import sleep as sl
print("hello")
sl(5)
print("world")