# s = '哈哈哈'
# print(dir(s))
# print(dir(str))

# lst = [1,2,3]
# lst_iter = lst.__iter__()
# from collections import Iterable    #可迭代
# from collections import Iterator    #迭代器
#
# print(isinstance(lst, Iterable))    #True
# print(isinstance(lst, Iterator))    #false
# print(isinstance(lst_iter, Iterable))   #True
# print(isinstance(lst_iter, Iterator))   #True


# s = '我爱北京天安门'
# c = s.__iter__()  #获取迭代器
# print(c.__next__())     #使用迭代器进行迭代，获取第一个元素“我”
# print(c.__next__())     #   爱
# print(c.__next__())     #   北
# print(c.__next__())     #   京
# print(c.__next__())     #   天
# print(c.__next__())     #   安
# print(c.__next__())     #   门

# for i in [1,2,3]:
#     print(i)

# 使用while+迭代器来模拟for循环
lst = [1,2,3]
lst_iter = lst.__iter__()
while 1:
    try:
        i = lst_iter.__next__()
        print(i)
    except  StopIteration:
        break
