# 打开一个文件对象，并读取文件
fr=open("08-Python文件操作/src/bill.txt","r",encoding="utf-8")

# 打开另一个文件对象，用于文件写出
fw=open("08-Python文件操作/src/bill.txt.bak","w",encoding="utf-8")

# for 循环内容，判断是否是测试，不是测试就 write 写出，是测试就 continue 跳过
for line in fr:
    line=line.strip()
    if line.split(",")[-1]=="测试":
        continue
    else:
        fw.write(line)
        # 由于前面对内容进行了strip的操作，所以要手动写出换行符
        fw.write("\n")

# 将2个文件对象均 close()
fr.close()
fw.close()