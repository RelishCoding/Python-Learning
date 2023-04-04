# 导入自定义模块进行使用
# import my_module1
# my_module1.test(1,2)
# from my_module1 import test
# test(1,2)

# 导入不同模块的同名功能
# from my_module1 import test
# from my_module2 import test
# test(1,2)

# __main__变量
# from my_module1 import test

# __all__变量
from my_module1 import * 
test_a(1,2)