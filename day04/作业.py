# 1.写代码，有如下列表，按照要求实现每一个功能
# li = ['alex','WuSir','ritian','barry','wenzhou']
# 1)计算列表的长度并输出
# 2)列表中追加元素”seven”,并输出添加后的列表
# 3)请在列表的第1个位置插入元素”Tony”,并输出添加后的列表
# 4)请修改列表第2个位置的元素为”Kelly”，并输出修改后的列表
# 5)请将列表l2=[1,”a”,3,4,”heart”]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# 6)请将字符串s=”qwer”的每一个元素添加到列表li中，一行代码现实，不允许循环添加。
# 7)请删除列表中元素”ritian”,并输出添加后的列表
# 8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表。
# 9)请删除列表中的第2至第4个元素，并输出删除元素后的列表。
# 10)请将列表所有的元素反转，并输出反转后的列表
# 11)请计算出”alex”元素在列表li中出现的次数，并输出该次数

li = ['alex','WuSir','ritian','barry','wenzhou']
print("1.计算列表的长度并输出")
print(len(li))

print('2.列表中追加元素”seven”,并输出添加后的列表')
li.append('seven')
print(li)

print('3.请在列表的第1个位置插入元素”Tony”,并输出添加后的列表')
li.insert(1,'Tony')
print(li)

print('4.请修改列表第2个位置的元素为”Kelly”，并输出修改后的列表')
li[2] = 'Kelly'
print(li)

print('5.请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。')
l2 = [1,'a',3,4,'heart']
li.extend(l2)
print(li)

print('6.请将字符串s="qwer"的每一个元素添加到列表li中，一行代码现实，不允许循环添加。')
s = "qwer"
li.extend(s)
print(li)

print('7.请删除列表中元素”ritian”,并输出添加后的列表')
li.remove("ritian")
print(li)

print('8.请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表。')
sn = li.pop(2)
print('sn='+sn)
print(li)

print('9.请删除列表中的第2至第4个元素，并输出删除元素后的列表。')
del li[2:4]
print(li)

print('10.请将列表所有的元素反转，并输出反转后的列表')
li.reverse()
print(li)

print('11.请计算出”alex”元素在列表li中出现的次数，并输出该次数')
num = li.count("alex")
print(num)


# 2.写代码，有如下列表，利用切片实现每一个功能
#     li = [1,3,2,'a',4,'b',5,'c']
# 1)通过对li列表的切片形成新的列表l1,l1=[1,3,2]
# 2)通过对li列表的切片形成新的列表l2,l2=[‘a’,4,’b’]
# 3)通过对li列表的切片形成新的列表l3,l3=[1,2,4,5]
# 4)通过对li列表的切片形成新的列表l4,l4=[3,’a’,’b’]
# 5)通过对li列表的切片形成新的列表l5,l5=[‘c’]
# 6)通过对li列表的切片形成新的列表l6,l6=[‘b’,’a’,3]

li = [1,3,2,'a',4,'b',5,'c']
print(li)
print('1.通过对li列表的切片形成新的列表l1,l1=[1,3,2]')
l1 = li[:3]
print(l1)

print('2.通过对li列表的切片形成新的列表l2,l2=[‘a’,4,’b’]')
l2 = li[3:6]
print(l2)

print('3.通过对li列表的切片形成新的列表l3,l3=[1,2,4,5]')
l3 = li[::2]
print(l3)

print('4.通过对li列表的切片形成新的列表l4,l4=[3,’a’,’b’]')
l4 = li[1:6:2]
print(l4)

print('5.通过对li列表的切片形成新的列表l5,l5=[‘c’]')
l5 = li[-1:]
print(l5)

print('6.通过对li列表的切片形成新的列表l6,l6=[‘b’,’a’,3]')
l6 = li[-3::-2]
print(l6)


# 3.写代码，有如下列表，按照要求实现每一个功能
#     lis = [2,3,'k',['qwer',20,['k1',['tt',3,'1']],89],'ab','adv']
# 1)将列表lis中的’tt’变成大写(用两种方式)
# 2)将列表中的数字3变成字符串’100’(用两种方式)
# 3)将列表中的字符串’1’,变成数字101(用两种方式)
lis = [2,3,'k',['qwer',20,['k1',['tt',3,'1']],89],'ab','adv']
print(lis)
print('1.将列表lis中的’tt’变成大写(用两种方式)')
print('第一种：')
print(lis[3][2][1][0].upper())
print('第二种：')
lis[3][2][1][0] = 'TT'
print(lis)


print('2.将列表中的数字3变成字符串’100’(用两种方式)')
print('第一种：')
# lis[3][2][1][1] = 100
# print(lis)
print('第二种：')
lis[3][2][1][1] = str(lis[3][2][1][1] + 97)
print(lis)

print('3.将列表中的字符串’1’,变成数字101(用两种方式)')
print('第一种：')
# lis[3][2][1][2] = 101
# print(lis)
print('第二种：')
lis[3][2][1][2] = int(lis[3][2][1][2]) + 100
print(lis)

# 4.请用代码实现：
# li=['alex','eric','rain']
# 利用下划线将列表的每一个元素拼接成字符串’alex_eric_rain’
print('利用下划线将列表的每一个元素拼接成字符串 alex_eric_rain')
li = ['alex','eric','rain']
print(li)
s = ''
for el in li:
    s = s + el + "_"
print(s[:-1])


# 5.利用for循环和range打印出下面列表的索引。
# li=[‘alex’,’WuSir’,’ritian’,’barry’,’wenzhou’]
li = ['alex','WuSir','ritian','barry','wenzhou']

print('range')
for el in range(len(li)):
    print(el)

print('------------------------')

# 6.利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
li = []
for el in range(101):
    if el%2 == 0:
        li.append(el)
print(li)

# 7.利用for循环和range找出50以内能被3整除的数，并将这些数插入到一个新列表中。
print('---------------7-----------------')
li = []
for el in range(51):
    if el % 3 == 0:
        li.append(el)
print(li)

# 8.利用for循环和range从100-1，倒序打印
print('---------------8-----------------------')
for el in range(100,0,-1):
    print(el)

# 9.利用for循环和range从100-10，倒序将所有的偶数添加到一个新列表中，
#     然后对列表的元素进行筛选，将能被4整除的数留下来。
li = []
print('---------------9--------------')
for el in range(100,9,-1):
    if el % 2 == 0:
        li.append(el)
        for i in li:
            if i % 4 != 0:
                li.remove(i)
print(li)

# 10.利用for循环和range，将1-30的数字一次添加到一个列表中，
#     并循环这个列表，将能被3整除的数改成*。
print('-----------------------10--------------------')

li = []
for i in range(1,31):
    li.append(i)
for el in li:
    if el % 3 == 0:
        li[li.index(el)] = '*'
print(li)


