# 文件处理相关的工具模块

def print_file_info(file_name):
    """
    功能：将给定路径的文件内容输出到控制台中
    :param file_name: 即将读取的文件路径
    :return: None
    """
    f=None
    try:
        f=open(file_name,"r",encoding="utf-8")
        content=f.read()
        print("文件的全部内容如下：")
        print(content)
    except Exception as e:
        print(f"程序出现异常了，原因是：{e}")
    finally:
        if f:
            f.close()

def append_to_file(file_name,data):
    """
    功能：将给定的数据追加到指定的文件中
    :param file_name: 指定的文件路径
    :param data: 指定的数据
    :return: None
    """
    f=open(file_name,"a",encoding="utf-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__=='__main__':
    print_file_info("D:/bill.txt")
    append_to_file("D:/teat_append.txt","黑马程序员")