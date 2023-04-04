# 打开一个不存在的文件
f=open("08-Python文件操作/src/test.txt","w",encoding="utf-8")
# write写入
f.write("hello world")
# flush刷新
f.flush()
# close关闭
f.close()

# 打开一个存在的文件
f=open("08-Python文件操作/src/test.txt","w",encoding="utf-8")
# write写入，flush刷新
f.write("hello python")
f.flush()
# close关闭
f.close()