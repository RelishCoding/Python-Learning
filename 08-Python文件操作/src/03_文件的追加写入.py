# 打开不存在的文件
f=open("08-Python文件操作/src/test.txt","a",encoding="utf-8")
f.write("hello world")
f.flush()
f.close()

# 打开存在的文件
f=open("08-Python文件操作/src/test.txt","a",encoding="utf-8")
f.write("\nhello python")
f.close()