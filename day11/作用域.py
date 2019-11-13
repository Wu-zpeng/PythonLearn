a = 100
def func():
    a = 40
    b = 20
    def abc():
        print('哈哈')
    print(a,b)  # 这里使用的是局部作用域
    print(globals())    #打印全局作用域的内容
    print(locals())     #打印局部作用域中的内容
func()


