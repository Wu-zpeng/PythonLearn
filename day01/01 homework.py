#1.使用while循环输出 1 2 3 4 5 6 8 9 10

'''
count = 0
while count < 10:
    count += 1
    if count == 7:
        continue
    print(count)
'''

#2.求1-100的所有数的和

'''
count = 0
sum_count = 0
while count < 100:
    count += 1
    sum_count += count
print(sum_count)

'''


#3.输出1-100内的所有奇数
'''
#方法一:
# count = 1
# while count < 101:
#     print(count)
#     count+=2

#方法二:
count = 1
while count < 100:
    if count % 2==1:
        print(count)
    count +=1

'''


#4.求1-100内的所有偶数
'''
count = 1
while count <101:
    if count % 2 == 0:
        print(count)
    count+=1
'''

#5.求1-2+3-4+5...99的所有数的和
'''
count = 1
total = 0;
while count < 100:
    if count %2 ==0:
        total = total-count
    else:
        total +=count
    count +=1
print(total)
'''

#6.用户登录（三次机会重试）

count = 1
while count < 4:
    name = input('请输入用户名:')
    password = input("请输入密码:")

    if name == '小二' and password =='123':
        print('登录成功')
        break
    else:
        print("登录失败，剩余"+str(3-count)+"机会")
    count+=1

