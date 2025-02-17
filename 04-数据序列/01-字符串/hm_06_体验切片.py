# 序列名[开始位置的下标:结束位置的下标:步长]

str1 = '012345678'
print(str1[2:5:1])  # 234
print(str1[2:5:2])  # 24
print(str1[2:5])  # 234
print(str1[:5])  # 01234 -- 如果不写开始，默认从0开始选取
print(str1[2:])  # 2345678 -- 如果不写结束，表示选取到最后
print(str1[:])  # 012345678 -- 如果不写开始和结束，表示选取所有

# 负数测试
print(str1[::-1])  # 876543210 -- 如果步长为负数，表示倒叙选取
print(str1[-4:-1])  # 567 -- 下标-1表示最后一个数据，依次向前类推

# 终极测试
print(str1[-4:-1:1])  # 567
print(str1[-4:-1:-1])  # 不能选取出数据：从-4开始到-1结束，选取方向为从左到右，但是-1步长：从右向左选取
# **** 如果选取方向(下标开始到结束的方向) 和 步长的方向冲突，则无法选取数据


print(str1[-1:-4:-1])  # 876







