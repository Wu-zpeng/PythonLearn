
#列表推导式  ：[ 结果 for循环 判断]
# lst = []
# for el in range(0,10):
#     lst.append(el)
# print(lst)
#
# #使用推导式
# lst = [el for el in range(0,11)]
# print(lst)
#
# #获取1-100内所有的偶数
# lst = [el for el in range(1,101) if el%2 == 0]
# print(lst)


# 寻找名字中带有两个e的⼈的名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven','Joe'],
            ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

# 普通算法
# lst = []
# for name in names:
#     for el in name:
#         if el.count('e') == 2:
#             lst.append(el)
# print(lst)

#使用推导式
# lst = [el for name in names for el in name if el.count('e') == 2]
# print(lst)


#   字典推导式
# 把字典中的key和value互换
dic = {'a': 1, 'b': '2'}
new_dic = {v:k for k,v in dic.items()}
print(new_dic)

# 在以下list中. 从lst1中获取的数据和lst2中相对应的位置的数据组成⼀个新字典
lst1 = ['jay', 'jj', 'sylar']
lst2 = ['周杰伦', '林俊杰', '邱彦涛']

#使用推导式
dic = { lst1[el]:lst2[el] for el in range(len(lst1))}
print(dic)

#普通算法
# dic = {}
# for el in range(len(lst1)):
#         dic[lst1[el]] = lst2[el]
# print(dic)


#   集合推导式
lst = [-1,1,8,-8,8]
s = {i for i in lst}
print(s)

