# def func():
#     print(111)
#     yield 222

# ret = func()
# print(ret)      #打印的是生成器地址
# gener = ret.__next__()
# print(gener)    #通过 __next__来取值，和迭代器一样

# def fun():
#     print(111)
#     yield 222
#     print(333)
#     yield 444
#
# gen = fun()
# ret = gen.__next__()
# print(ret)
# ret = gen.__next__()
# print(ret)

#普通函数，一次性打印全部
# def cloth():
#     lst = []
#     for i in range(0,100):
#         lst.append("衣服"+str(i))
#     return lst
# cl = cloth()
# print(cl)

#生成器函数需要的时候再取，省内存
# __next__ 让生成器执行到下一个yield
# def cloth2():
#     for i in range(0,100):
#         yield "衣服"+str(i)
# cl  = cloth2()
# ret = cl.__next__()
# print(ret)
# ret = cl.__next__()
# print(ret)

#   send方法
# def eat():
#     print('我吃什么？')
#     a = yield '馒头'
#     print('a='+a)
#     b = yield '饺子'
#     print('b='+ b)
#     c = yield '韭菜盒子'
#     print('c='+ c)
#     yield 'GAME OVER'
# gen = eat()     #获取生成器
# ret1 = gen.__next__()  #第一个元素
# print(ret1)
# ret2 = gen.send('胡辣汤')
# print(ret2)
# ret3 = gen.send('狗粮')
# print(ret3)
# ret4 = gen.send('猫粮')
# print(ret4)

#send() 和 __next__区别
#1.send和__next__都是让生成器向下走一次
#2.send可以给上一个yield的位置传递值，不能给最后一个yield发送值，在第一次执行生成器代码时不能用send()

#生成器可以使用for循环获取内部元素
def func():
    print(111)
    yield 222
    print(333)
    yield 444
gen = func()
for el in gen:
    print(el)

