
# 1.字符串：str.join()
# s = "_".join(li) > 》将列表使用"_"分隔符来将li列表变成字符串        》李嘉诚_李晨_黄海峰_刘嘉玲
#s = "_".join(str) >  将字符串str使用"_"分隔符来分割str，组成新的字符串 》黄_花_大_闺_女
# li = ["李嘉诚","李晨","黄海峰","刘嘉玲"]
# s = "_".join(li)
# print(s)
#
# print("------------------")
#
# str = "⻩花⼤闺⼥"
# s = "_".join(str)
# print(s)


# 2. 循环删除列表中的每一个元素
# li = [11,22,33,44]
# for e in  li:
#     li.remove(e)
# print(li)

# 报错
# i= 0, 1, 2 删除的时候li[0] 被删除之后. 后面一个就变成了第0个.
# 以此类推. 当i = 2的时候. list中只有1个元素. 但是这个时候删除的是第2个 肯定报错啊
# li = [11,22,33,44]
# for i in range(0,len(li)):
#     del li[i]
# print(li)

# 使用pop()也不可以
# li = [11,22,33,44]
# for i in li:
#     li.pop()
# print(li)

# 这样是可以删除，循环len(li)次, 然后从后往前删除
# li = [11,22,33,44]
# for i in range(0,len(li)):
#     li.pop()
# print(li)

# 用另一个列表来记录你要删除的内容. 然后循环删除
# li = [11,22,33,44]
# del_li = []
# for el in li:
#     del_li.append(el)
# for i in del_li:
#     li.remove(i)
# print(li)


# 3.dict中的fromkey(),可以帮我们通过list来创建一个dict
dic = dict.fromkeys(["jay","JJ"],["周杰伦","麻花藤"])
print(dic)  #前面列表中的每一项都会作为key, 后面列表中的内容作为value. 生成dict
# 结果    {'jay': ['周杰伦', '麻花藤'], 'JJ': ['周杰伦', '麻花藤']}

dic.get("jay").append("胡大")
print(dic)
# 结果    {'jay': ['周杰伦', '麻花藤', '胡⼤'], 'JJ': ['周杰伦', '麻花藤', '胡⼤']}
#代码中只是更改了jay那个列表. 但是由于jay和JJ用的是同一个列表. 所以. 前面那个改了. 后
# 面那个也会跟着改


# 4.dic中的元素在迭代过程中是不允许进行删除的  》dictionary changed size during iteration
# dic = {"k1":"alex","k2":"wusir","s1":"金老板"}
#删除key中带有"k"的元素
# for k in dic:
#     if 'k' in k :
#         del dic[k]
# print(dic)

# 办法：把要删除的元素暂时先保存在一个list中，然后循环list，再删除
# dic = {"k1":"alex","k2":"wusir","s1":"金老板"}
# dic_del_list = []
# # 删除key中带有'k'的元素
# for k in dic:
#     if 'k' in k:
#         dic_del_list.append(k)
# for i in dic_del_list:
#     del dic[i]
# print(dic)

# 5.类型转换：
# 元组 ==> 列表     list(tuple)
# 列表 ==> 元组     tuple(list)

# list ==> str      str.join(list)
# str ==> list      str.split()

# 转换成False的数据
# 0,'',None,[],(),{},set() ===> False




