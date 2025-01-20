mystr = "hello world and itcast and itheima and Python"

# 1. capitalize() 字符串首字母大写
new_str = mystr.capitalize()
print(new_str) #Hello world and itcast and itheima and python

# 2.title(): 字符串中每个单词首字母大写
new_str = mystr.title()
print(new_str) #Hello World And Itcast And Itheima And Python

# 3. upper()：小写转大写
new_str = mystr.upper()
print(new_str) #HELLO WORLD AND ITCAST AND ITHEIMA AND PYTHON

# 4. lower(): 大写转小写
new_str = mystr.lower()
print(new_str) #hello world and itcast and itheima and python

mystr = "   hello world and itcast and itheima and Python   "
print(mystr)
# 1. lstrip(): 删除左侧空白字符
new_str = mystr.lstrip()
print(new_str) #hello world and itcast and itheima and Python

# 2. rstrip(): 删除右侧空白字符
new_str = mystr.rstrip()
print(new_str) #   hello world and itcast and itheima and Python

# 3.strip()：删除两侧空白字符
new_str = mystr.strip()
print(new_str) #hello world and itcast and itheima and Python

