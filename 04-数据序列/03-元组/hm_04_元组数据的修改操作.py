t1 = ('aa', 'bb', 'cc', 'bb')


# t1[0] = 'aaa'   # 元组数据不能修改

t2 = ('aa', 'bb', ['cc', 'dd'])
print(t2[2])
print(t2[2][0])
t2[2][0] = 'TOM'    # 元组数据中的列表数据可以修改
print(t2)

