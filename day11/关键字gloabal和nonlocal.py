a = 10
def func():
    global a       #加了gloabal表示不再局部创建这个变量，而是直接使用全局a
    a = 28
    print(a)

# func()
# print(a)

#对于可变数据类型可以直接进行访问. 但是不能改地址. 说白了. 不能赋值
# lst = ['麻花藤','刘嘉玲','詹姆斯']
# def func1():
#     lst.append('马云')
#     print(lst)

# func1()
# print(lst)


#nonlocal
a = 10
def func1():
    a = 20
    def func2():
        nonlocal a
        a = 30
        print(a)
    func2()
    print(a)
func1()


a = 1
def fun_1():
    a = 2
    def fun_2():
        nonlocal a
        a = 3
        def fun_3():
            a = 4
            print(a)
        print(a)
        fun_3()
        print(a)
    print(a)
    fun_2()
    print(a)
print(a)
fun_1()
print(a)





