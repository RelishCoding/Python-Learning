# 基本捕获语法
try:
    f=open("abc.txt","r",encoding="utf-8")
except:
    print("出现异常了，因为文件不存在，改为w模式打开")
    f=open("09-异常模块与包/src/abc.txt","w",encoding="utf-8")

    
# 捕获指定的异常
try:
    print(name)
    # 1/0
except NameError as e:
    print("出现了变量未定义异常")
    print(e)

# 捕获多个异常
try:
    # 1/0
    print(name)
except(NameError,ZeroDivisionError) as e:
    print("出现了变量未定义或者除以0的异常")

# 捕获所有异常
try:
    # 1/0
    # print(name)
    f=open("123.txt","r",encoding="utf-8")
except Exception as e:
    print("出现异常了")
    f=open("D:123/.txt","w",encoding="utf-8")
else:
    print("好高兴，没有异常")
finally:
    print("我是finlly，有没有异常我都要执行")
    f.close()