
a = 10
print(type(a))
s = str(a)  #数字变成字符串
print(type(s))

#想把某数据转换成xxx数据类型。   xxx(数据)


a = 0   #false
print(bool(a))

#空字符串是false
s = "哈哈"
print(bool(s)) # True

#总结：空的东西是false，非空的东西是true

lst = [1] #空列表是false
print(bool(lst))


b = None #表示空，真空
print(bool(b))


'''
    总结：
    1：所有的空都是false，所有的非空都是true
    2：想把某数据转成xxx数据类型， xxx(数据)
        例如：str => int  :字符串转int类型 
                a = int(s)
'''

