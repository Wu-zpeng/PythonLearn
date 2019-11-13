def func1():
    print('111')
def func2():
    print('2222')
    func1()
#
# func2()
# print(111)

def fun2():
    print(222)
    def fun3():
        print(666)
    print(444)
    fun3()
    print(888)
print(333)
fun2()
print(555)
