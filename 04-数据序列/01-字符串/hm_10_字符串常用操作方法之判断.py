mystr = "hello world and itcast and itheima and Python"

# 1. startswith(): 判断字符串是否以某个子串开头
print(mystr.startswith('hello'))    # True
print(mystr.startswith('hel'))  # True
print(mystr.startswith('hels')) # False


# 2. endswith(): 判断字符串是否以某个子串结尾
print(mystr.endswith('Python')) # True
print(mystr.endswith('Pythons'))    # False


# 3. isalpha(): 字母
print(mystr.isalpha())  # False

# 4. isdigit(): 数字
print(mystr.isdigit())  # False
mystr1 = '12345'
print(mystr1.isdigit()) # True

# 5. isalnum() : 数字或字母或组合
print(mystr1.isalnum()) # True
print(mystr.isalnum())  # False
mystr2 = 'abc123'
print(mystr2.isalnum())   # True


# 6.isspace(): 空白
print(mystr.isspace())    # False
mystr3 = '   '
print(mystr3.isspace()) # True

