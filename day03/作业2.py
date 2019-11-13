# 2.	有字符串s=”123a4b5c”
# 1)	通过对s切片形成新的字符串s1，s1=”123”
# 2)	通过对s切片形成新的字符串s2，s2=”a4b”
# 3)	通过对s切片形成新的字符串s3，s3=”1345”
# 4)	通过对s切片形成字符串s4，s4=”2ab”
# 5)	通过对s切片形成字符串s5，s5=”c”
# 6)	通过对s切片形成字符串s6，s6=”ba2”

s = '123a4b5c'
s1 = s[:3]
print('s1='+s1)
s2 = s[3:6]
print('s2='+s2)
s3 = s[:7:2]
print('s3='+s3)
s4 = s[1:6:2]
print('s4='+s4)
s5 = s[-1:]
print('s5='+s5)
s6 = s[-3:-8:-2]
print('s6='+s6)

print('-------------')

# 3.使用while和for循环分别打印字符串s=”asdfer”中的每个元素
s = 'asdfer'
count = 0
while count < len(s):
    print(s[count])
    count += 1
print('--------')

print('---------for循环-------')
for i in s:
    print(i)

# 4.使用for循环对s=”asdfer”进行循环，但是每次打印的内容都是”asdfer”
print('--------4----------------')
s = 'asdfer'
for i in s:
    print(s)

# 5.使用for循环对s=”abcdefg”进行循环，每次打印的内容是每个字符加上sb，
# # 例如: asb,bsb,csb,…gsb
print('--------5--------')
s = 'abcdefg'
for i in s:
    print(i+'sb')

# 6.使用for循环对s=”321”进行循环，打印的内容依次是:”倒计时3秒”， ”倒计时2秒”，
# ”倒计时1秒”, ”出发！”。
print('---------6-----------')
s = '321'
for i in s:
    print('倒计时%s秒'%i)
else:
    print('出发！')

# 7.实现一个整数加法计算器（两个数相加）
# 如：content=input(“请输入内容:”) 用户输入：5+9或5+ 9或5 +9，然后进行分割再计算
# print('------7---------')
# content = input('请输入内容：')
# s = content.strip(" ")
# lst = s.split('+')
# print(int(lst[0]) + int(lst[1]))

# 8.升级题：实现一个整数加法计算器（多个数相加）
# 如：content=input(“请输入内容:”)  用户输出：5+9+6 +12+  13，然后进行分割再计算
# print('---------8------------')
# content = input('请输入内容：')
# s = content.strip()
# lst = s.split('+')
# sum = 0;
# for i in lst:
#     sum += int(i)
# print(sum)

# 9.计算用户输入的内容中有几个整数（以个数为单位）
# 如：content=input(“请输入内容:”)   #fhdal234slfh98769fjdla
# print('---------9------------')
# content = input('请输入内容：')
# count = 0
# for i in content:
#     if i.isdigit():
#         count += 1
# print(count)

# 10.写代码，完成下列需求：
# 用户可持续输入（用while循环），用户使用的情况：
# 输入A，则显示走大路回家，然后在让用户进一步选择：
# 		是选择公交车，还是步行？
# 		选择公交车，显示10分钟到家，并退出整个程序。
# 		选择步行，显示20分钟到家，并退出整个程序。
# 输入B，则显示走小路回家，并退出整个程序。
# 输入C，则显示绕道回家，然后在让用户进一步选择：
# 		是选择游戏厅玩会，还是网吧？
# 		选择游戏厅，则显示“一个半小时到家，爸爸在家，拿棍等你”。并让其重新输入A,B,C选项。
# 		选择 网吧，则显示“两个小时到家，妈妈已做好了战斗准备。”并让其重新输入A,B,C选项。
# print('----------10-----------')
# content = input('请输入回家路线：')
# while 1:
#     if content == 'A':
#         print('走大路回家。')
#         traff = input('选择公交车还是步行？')
#         if traff == '公交车':
#             print('10分钟到家。')
#             break
#         elif traff == '步行':
#             print('20分钟到家。')
#             break
#     elif content == 'B':
#         print('走小路回家。')
#         break
#     elif content =='C':
#         print('绕道回家。')
#         s1 = input('是选择游戏厅玩会，还是网吧？')
#         if s1 == '游戏厅':
#             print('一个半小时到家，爸爸在家，拿棍等你。')
#             break
#         elif s1 == '网吧':
#             print('两个小时到家，妈妈已做好了战斗准备。')
#             break
#         else:
#             print('洗澡？？？')
#             break
#     else:
#         print('回家洗洗睡吧。')
#         break

# 11.写代码：计算1 – 2 + 3 … + 99 中除了88以外所有数的总和？
print('----------11------------')
sum = 0
count = 0
while count <=99:
    if count == 88:
        count += 1
        continue
    if count%2 == 0:
        sum -= count
    else:
        sum += count
    count += 1
print(sum)

# 12.（升级题）判断一句话是否是回文，回文：正着念和反着是一样的。例如，上海自来水来自海上（升级题）
# print('---------12------------')
# content = input("请输入内容：")
# count = len(content)
# s = content[:-(count+1):-1]
# if content == s:
#     print('这句话是回文')
# else:
#     print('不是回文')

# 13.输入一个字符串，要求判断在这个字符串中大写字母，小写字母，数字，其他字符共出现了多少次，并输出出来
# print('--------13-----------')
# content = input("请输入内容：")
# daxie = 0
# xiaoxie = 0
# num = 0
# other = 0
#
# for c in content:
#     if c.isupper():
#         daxie += 1
#     elif c.islower():
#         xiaoxie += 1
#     elif c.isdigit():
#         num += 1
#     else:
#         other += 1
# print('大写字母有%d个'% daxie)
# print('小写字母有%d个'% xiaoxie)
# print('数字有%d个'% num)
# print('其他有%d个'% other)

# 14.制作趣味模板程序需求：等待用户输入名字、地点、爱好，
#     根据用户的名字和爱好进行任意显示 如：敬爱可亲的XXX，最喜欢在XXX地方干XXX
print('-----------14-------------')
name = input("请输入名字：")
adress = input('请输入地点：')
hobby = input('请输入爱好：')
print('敬爱可亲的%s，最喜欢在%s地方干%s'%(name,adress,hobby))
print('敬爱可亲的{}，最喜欢在{}地方干{}'.format(name,adress,hobby))
