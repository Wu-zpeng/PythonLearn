s13 = "我叫sylar, 我喜欢python, java, c等编程语⾔."
ret = s13.find("a",8,22)
print(ret)

s1 = "alex Is LOSER DOG"
# ret1 = s1.capitalize()
# print(ret1)

ret2 = s1.swapcase();
print(ret2)

# 练习. ⽤算法判断某⼀个字符串是否是⼩数
s17 = "-123.12"
s2 = s17.replace("-","")
if s2.isdigit():
    print('是整数')
else:
    if s2.count('.') == 1 and not s2.startswith('.') and not s2.endswith('.'):
        print('是小数')
    else:
        print('不是小数')

print('-------------')

s20 = "I am sylar, I'm 14 years old, I have 2 dogs!"
count = 0
for c in s20:
    if c.isdecimal():
        count += 1
print(count)





