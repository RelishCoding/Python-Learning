import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("黑马程序员"))
print(my_utils.str_util.substr("黑马程序员",0,4))

file_util.print_file_info("D:test_append.txt")
file_util.append_to_file("D:test_append.txt","itheima")