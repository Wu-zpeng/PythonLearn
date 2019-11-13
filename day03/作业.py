# 1.	有变量name =”aleX leNb”完成如下操作：
#
# 1)	移除name变量对应的值两边的空格，并输出处理结果
# 2)	移除name变量左边的”al”并输出处理结果
# 3)	移除name变量右边的”Nb”，并输出处理结果
# 4)	移除name变量开头的”a”与最后的”b”，并输出处理结果
# 5)	判断name变量是否以”al”开头，并输出处理结果
# 6)	判断name变量是否以”Nb”结尾，并输出处理结果
# 7)	将name变量对应的值中的所有的”l”替换为”p”，并输出处理结果
# 8)	将name变量对应的值中的第一个”l”替换成”p”，并输出结果
# 9)	将name变量对应的值根据所有的”l”分割，并输出结果
# 10)	将name变量对应的值根据第一个”l”分割，并输出结果
# 11)	将name变量对应的值变大写，并输出结果
# 12)	将name变量对应的值变小写，并输出结果
# 13)	将name变量对应的值首字母”a”大写，并输出结果
# 14)	判断name变量对应的值字母”l”出现几次，并输出结果
# 15)	如果判断name变量对应的值前四位”l”出现几次，并输出结果
# 16)	从name变量对应的值中找到”N”对应的索引(如果找不到则报错)，并输出结果
# 17)	从name变量对应的值中找到”N”对应的索引(如果找不到则返回-1)并输出结果
# 18)	从name变量对应的值中招到”X le”对应的索引，并输出结果
# 19)	请输出name变量对应的值第2个字符？
# 20)	请输出name变量对应的值前3个字符？
# 21)	请输出name变量对应的值后2个字符？
# 22)	请输出name变量对应的值中”e”所在的索引位置

name ='aleX leNb'
s1 = name.strip()
print('s1='+s1)
print('----------')

s2 = name.strip('al')
print('s2='+s2)
print('----------')

s3 = name.rstrip('Nb')
print('s3='+s3)
print('----------')

s4 = name.lstrip('a').rstrip('b')
print('s4='+s4)
print('----------')

print(name.startswith('al'))
print(name.endswith('Nb'))
print('----------')

s7 = name.replace('l','p')
print('s7='+s7)
print('----------')

s8 = name.replace('l','p',1)
print('s8='+s8)
print('----------')

ls1 = name.split('l')
print(ls1)
print('----------')

ls2 = name.split('l',1)
print(ls2)
print('----------')

s11 = name.upper()
print('s11='+s11)
print('----------')

s12 = name.lower()
print('s12='+s12)
print('----------')

s13 = name.capitalize()
print('s13='+s13)
print('----------')

count = name.count('l')
print(count)
print('----------')

num = name.count('l',0,4)
print(num)
print('----------')

count = name.index('N')
print(count)
print('----------')

count = name.find('N')
print(count)
print('----------')

count = name.find('X le')
print(count)
print('----------')

s19 = name[1]
print('s19='+s19)
print('----------')

s20 = name[:3]
print('s20='+s20)
print('----------')

s21 = name[-2:]
print('s21='+s21)
print('----------')

count = name.index('e')
print(count)

