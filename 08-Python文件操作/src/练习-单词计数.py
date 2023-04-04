count=0
with open("08-Python文件操作/src/word.txt","r",encoding="UTF-8") as f:
    # 方法1
    #content=f.read()
    #count=content.count("itheima")
    
    # 方法2
    for line in f:
        line=line.strip()#去除开头和结尾的空格以及换行符
        # 注意若不strip列表最后一个字符串会带有"\n"
        list=line.split(' ')
        for l in list:
            if l=="itheima":
                count=count+1
print(count)
