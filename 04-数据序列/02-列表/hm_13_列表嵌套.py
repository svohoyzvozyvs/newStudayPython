name_list = [['TOM', 'Lily', 'Rose'], ['张三', '李四', '王五'], ['xiaohong', 'xiaoming', 'xiaolv']]

# print(name_list)

# 列表嵌套的时候的数据查询
# print(name_list[0])
print(name_list[0][1])

for name in name_list:
    if  type(name) == list:
        for e in name:
            print(e)
    else:
        print(name)