# def func():
#     print(222)
# print(func)

# def func():
#     print(111)
# print(func)
#
# a = func
# a()

# 函数名可以当做容器类的元素
# def func1():
#     print(111)
# def func2():
#     print(222)
# def func3():
#     print(333)
# lst = [func1, func2, func3]
# for el in lst:
#     el()


# 函数名可以当做函数的参数
# def func():
#     print('吃了么')
# def fun2(fn):
#     print('我 是fun2')
#     fn()    # 执行传递过来的fn
#     print("我是fun2")
# fun2(func)     # 把函数func当成参数传递给func2的参数fn.


# 函数名可以作为函数的返回值

def fun_1():
    print('这里是函数1')
    def fun_2():
        print('这里是函数2')
    print('这里是函数1')
    return fun_2

fn = fun_1()    # 执行函数1. 函数1返回的是函数2, 这时fn指向的就是上面函数2
fn()        # 执行上面返回的函数
