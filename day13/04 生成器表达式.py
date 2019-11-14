#   生成器表达式，没有元组推导式
gen = (el for el in range(10))
print(gen)  #打印的是生成器

# 获取1-100内能被3整除的数
# gen = (el for el in range(1,101) if el%3 == 0)
# for i in gen:
#     print(i)


def add(a, b):
    return a + b
def test():
    for r_i in range(4):
        yield r_i
g = test()
for n in [2, 10]:
 g = (add(n, i) for i in g)
print(list(g))

