# 二：set集合
# lst = [45,5,'哈哈',45,'哈哈',50]
# lst = list(set(lst))        #把list转换成set，然后再转换回list
# print(lst)

# (1)增加
# s_set = {"alex","wusir","Tom"}
# s_set.add('kiwi')
# s_set.add('wusir')      #重复的内容不会被添加
# print(s_set)

# s_set = {"alex","wusir","Tom"}
# s_set.update('麻花藤')
# print(s_set)
#
# s_set.update(['周杰伦',"林俊杰","大湿兄"])
# print(s_set)

# (2)删除
# s_set = {'alex','wusir','hello_kity','miki'}
# item = s_set.pop()  #随机弹出一个
# print(s_set)
# print(item)

# s_set = {'alex','wusir','hello_kity','miki'}
# s_set.remove('alex')    #直接删除元素
# s_set.remove('JJ')      #不存在这个元素，删除会报错
# print(s_set)

# s_set = {'alex','wusir','hello_kity','miki'}
# s_set.clear()   # 清空set集合.需要注意的是set集合如果是空的. 打印出来是set() 因为要和 dict区分的
# print(s_set)    #   set()

# （3）修改
# s = {"刘嘉玲", '关之琳', "王祖贤","张曼⽟", "李若彤"}
# #把刘嘉玲改成赵本山
# s.remove("刘嘉玲")
# s.add('赵本山')
# print(s)
#
# s = frozenset(["赵本山", "刘能", "⽪长山", "长跪"])
# dic = {s:'123'}
# print(dic)
#
# s = {"赵本山", "刘能", "⽪长山", "长跪"}
# dic = {s:'123'};
# print(dic)

# dic = {'JJ':'林俊杰','alex':'太白','wusir':'小伍'}
# dic['Kity'] = 'nihao'
# print(dic)

print('--------------------------------------')
s1 = {'刘能','赵四','皮长山'}
s2 = {'刘科长','冯乡长','皮长山'}

print('-------交集-------------')
print(s1 & s2)
print(s1.intersection(s2))  #{'皮长山'}

print('----并集-------------------')
print(s1 | s2)
print(s1.union(s2))     #{'刘科长', '皮长山', '冯乡长', '赵四', '刘能'}

print('-------差集-----------------')
print(s1 - s2)
print(s1.difference(s2))    #{'赵四', '刘能'}

print('----------反交集------------')
print(s1 ^ s2)
print(s1.symmetric_difference(s2))  #{'刘科长', '赵四', '冯乡长', '刘能'}

print('-------------------------------')

s1 = {'刘能','赵四'}
s2 = {'刘能','赵四','皮长山'}
print('-------子集-------------')
print(s1 < s2)      #True
print(s1.issubset(s2))

print('----------超集------------')
print(s1 > s2)
print(s1.issuperset(s2))    #False


