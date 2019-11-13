# 三.深浅拷贝
# 1.浅拷贝
lst1 = ['何灵','杜海涛','周渝民']
lst2 = lst1.copy()
lst1.append('李嘉诚')
print(lst1)
print(lst2)

print(id(lst1))
print(id(lst2))
# 结果：两个list完全不一样，内存地址和内容也不一样，发现实现了内存的拷贝

print('------------------------------------')

lst1 = ['何灵','杜海涛','周渝民',["麻花藤",'马云','周笔畅']]
lst2 = lst1.copy()
lst1[3].append('alex')
print(lst1)
print(lst2)
print(id(lst1[3]))
print(id(lst2[3]))
# 结果：第二层的内容地址是一样的

# 综上所述：
#     浅拷贝：只会拷贝第一层，第二层的内容不会拷贝，所以称为浅拷贝

# 2.深拷贝
import copy
print('-----------------深拷贝------------------------------------')
lst1 = ['何灵','杜海涛','周渝民',["麻花藤",'马云','周笔畅']]
lst2 = copy.deepcopy(lst1)
lst1[3].append('无敌是多么寂寞')
print(lst1)
print(lst2)
print(id(lst1[3]))
print(id(lst2[3]))
# 结果：都不一样了，深度拷贝，把元素内部的元素完全进行拷贝复制，不会产生一个改变另一个跟着改变的问题

print('---------题目------------------')
a = [1,2]
a[1] = a
print(a[1])
