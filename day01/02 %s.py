#格式化输出
# % s d : % 是占位符, s是字符串, d是数字
# name = input('请输入姓名:')
# age = input('请输入年龄:')
# height = input('请输入身高:')
# msg = '我叫%s, 今年%s, 身高 %s' %(name,age,height)
# print(msg)

"""
name = input('请输入姓名:')
age = input('请输入年龄:')
job = input('请输入职业:')
Hobbie = input('请输入爱好:')

msg = '''
------------ info of %s  -----------
Name  : %s
Age   : %d
job   : %s
Hobbie: %s
------------- end -----------------''' %(name,name,int(age),job,Hobbie)
print(msg)
"""

#想要在格式化输出中表示单纯的 % 就加一个%。前面的 % 代表转义，后面的 % 就是单纯的 %
# %% 只是单纯的显示 %
name = input('请输入姓名:')
age = input('请输入年龄:')
height = input('请输入身高:')
msg = '我叫%s, 今年%s, 身高 %s, 学习进度3%%' %(name,age,height)
print(msg)
