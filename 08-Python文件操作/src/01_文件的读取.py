# 打开文件
f=open("E:/测试.txt","r",encoding="UTF-8")
print(type(f))

# 读取文件-read
# 连续调用两次read方法，第二次会从第一次读取的内容末尾接着读取
# print(f"读取10个字节的结果是：{f.read(10)}")
# print(f"读取全部内容的结果是：{f.read()}")

# 读取文件-readlines
# 读取文件的全部行，封装到列表中
# lines=f.readlines()
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的内容：{lines}")

# 读取文件-readline
# line1=f.readline()
#line2=f.readline()
#print(line1)
#print(line2)

# for循环读取文件行
for line in f:
    print(f"每一行数据是：{line}")

# 文件的关闭
f.close()

# with open 语法操作文件
with open("E:/测试.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(line)