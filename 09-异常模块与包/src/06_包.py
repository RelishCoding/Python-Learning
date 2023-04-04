# 创建一个包

# 导入自定义的包中的模块
# import mypackage.my_module1
# import mypackage.my_module2
# mypackage.my_module1.info_print1()
# mypackage.my_module2.info_print2()

# from mypackage import my_module1
# from mypackage import my_module2
# my_module1.info_print1()
# my_module2.info_print2()

# from  mypackage.my_module1 import info_print1
# from  mypackage.my_module2 import info_print2
# info_print1()
# info_print2()

# 通过__all__ 变量，控制import *
from mypackage import * 
my_module1.info_print1()