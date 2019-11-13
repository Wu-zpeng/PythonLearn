
import os
# 2.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
def new_list_func(lis):
    new_list = []
    for i in range(len(lis)):
        if i%2 == 1:
            new_list.append(lis[i])
    return new_list

lis = ["alex","taibai","eric","kingdom","xinxin","xiaolaba"]
print(new_list_func(lis))

print("------------3-----------------")
# 3.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def length(lis):
    return len(lis) > 5

print(length(lis))

# 4.写函数，检查传入列表的长度，如果大于2，将列表的前两项内容返回给调用者
print('----------4-------------------')

def content_len(lis):
    new_lis = []
    if len(lis) > 2:
        new_lis.append(lis[0])
        new_lis.append(lis[1])
    else:
        return
    return new_lis

lis = ["alex","taibai","eric","kingdom","xinxin","xiaolaba"]
print(content_len(lis))

print('-----------5---------------')
# 5.写函数，计算传入函数的字符串中，数字、字母、空格以及其他内容的个数，并返回结果

def count(str):
    shuzi = 0
    zimu = 0
    kongke = 0
    qita = 0
    for i in str:
        if i.isdigit():
            shuzi += 1
        elif i.isalpha():
            zimu += 1
        elif i == " ":
            kongke += 1
        else:
            qita += 1
    return shuzi,zimu,kongke,qita

print(count('daujdfpaif  32132165@@@  '))

print('---------6---------------------')
# 6.写函数，接受两个数字参数，返回比较大的那个数字。
def compa_num(a,b):
    return a if a>b else b

print(compa_num(100,20))

print('--------------7-------------------')
# 7.写函数，检查传入字典的每一个value的长度，
# 如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic={‘k1’:’v1v1’,’k2’:[11,22,33,44]}
# Ps:字典中的value只能是字符串或列表

def new_dic_func(lis):
    new_dic = {}
    for key,value in lis.items():
        if len(value) > 2:
            new_dic[key] = value[0:2]
        else:
            new_dic[key] = value
    return new_dic

dic = {"alex":"小星星","taibai":"老牛吃草","JJ":"林俊杰","k2":[11,22,33,44]}
print(new_dic_func(dic))

print('-----------------8-----------------')
# 8.写函数，此函数只接收一个参数且此参数必须是列表数据类型，
# 此函数完成的功能是返回给调用者一个字典，此字典的键值对为此列表的索引及对应的元素。
# 例如传入的列表为：[11,22,33]，返回的字典为{0:11,1:22,2:33}。
def dic_func(lis):
    new_dic = {}
    if type(lis) == list:
        for i in range(len(lis)):
            new_dic[i] = lis[i]
        return new_dic
    else:
        return "不是列表"

lis = [11,22,33,44]
print(dic_func(lis))

print('-----------------9-------------------')
# 9.写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。
# 用户通过输入这四个内容，然后将这四个内容传入到函数中，
# 此函数接收到这四个内容，将内容追加到一个studentmsg文件中。

# 10.对第9题升级：支持用户持续输入，
# Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。

def file_func(name,gender,age,edu):
        with open("studentmsg.txt",mode="a",encoding="utf-8") as f1:
            f1.write(name + '_' + gender + '_' + age + '_' + edu + '\n')
        return '添加成功'

def file_func2(name,age,edu,gender="男"):
        with open("studentmsg.txt",mode="a",encoding="utf-8") as f1:
            f1.write(name + '_' + gender + '_' + age + '_' + edu + '\n')
        return '添加成功'

# while 1:
#     content = input('输入Q或者q就退出，其他符号继续进行：')
#     if content.upper() == 'Q':
#         break
#     else:
#         name = input('请输入姓名：')
#         gender = input('请输入性别：')
#         age = input('请输入年龄：')
#         edu = input('请输入学历：')
#         if gender == '男':
#             file_func2(name,age,edu)
#         else:
#             file_func2(name,age,edu,gender)

print('--------------11---------------------')
# 11.写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（升级题）
def file_reset(filenama,old,new):
    with open(filenama,mode='r',encoding='utf-8') as f1,\
        open(filenama+"_副本", mode="w",encoding='utf-8') as f2:
        for line in f1:
            line = line.replace(old,new)
            f2.write(line)
    os.remove(filenama)
    os.rename(filenama+"_副本",filenama)
    return '操作成功'

# print(file_reset("python好难","老男孩","千峰教育"))

print('----------------------12---------------------')
# 12.	写一个函数完成三次登录功能，再写一个函数完成注册功能（升级题）
# 注册：
# 首先要从文件中读取用户名和密码，匹配用户输入的用户名和文件中用户名是否一致，如果一致，提示重新输入。
# 其次，如果上面的判断没有问题，把用户名和密码写入文件中

def register():
    print('-----注册系统-------')
    while 1:
        username = input('请输入用户名：')
        password = input('请输入密码：')

        f = open("info.log",mode='r+',encoding='utf-8')
        for line in f:
            if line.split("@@")[0] == username:
                print('用户名已存在，请重新输入')
                break
        else:
            f.write('\n'+username + '@@' + password)
            print('注册成功')
            break

def landing():
    print('--------------登陆系统--------------')
    count = 1
    while count <= 3 :
        username = input('请输入用户名：')
        password = input('请输入密码：')

        f = open('info.log',mode='r',encoding='utf-8')
        for line in f:
            lis = line.strip().split("@@")
            if username == lis[0] and password == lis[1]:
                print('登陆成功,欢迎%s'% username)
                return
        else:
                print('用户名或密码错误。')
                count+=1
                continue

print('欢迎来到腾飞系统')
num = int(input('请选择登陆或者注册，1是登陆，2是注册'))
if num == 1:
    landing()
elif num == 2:
    register()
else:
    print('输入错误，请重新输入')



















