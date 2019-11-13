
 # 闭包就是内层函数, 对外层函数(非全局)的变量的引用. 叫闭包
# def func1():
#     name = 'alex'
#     def func2():
#         print(name) #闭包
#     func2()
#     print(func2.__closure__)    #返回cell就是闭包. 返回None就不是闭包
# func1()


from urllib.request import urlopen

def but():
    content = urlopen("http://www.xiaohua100.cn/index.html").read()
    def get_content():
        return content
    return get_content()
fn = but()     #这个时候就开始加载校花100的内容
#后面需要要用到这里面的内容就不需要在执行非常耗时的网络连接操作了
content = fn()  #获取内容
print(content)

content2 = fn()
print(content2)
