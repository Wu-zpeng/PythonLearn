dic = {}
dic['name'] = '周润发' # 如果dict中没有出现这个key, 就会新增⼀个key-value的组合进dict
dic['age'] = 18
print(dic)

print('--------------------------------------')

dic = {'id':123,'name':'sylar','age':18,'ok':'科比'}
print(dic.keys())
print(dic.values())
print(dic.items())

print('-------------------------------------------')
#
# 1.将name对应的列表追加一个元素'wysuir'
# 2.将name对应的列表中的alex首字母大写。
# 3.oldboy对应的字典加一个键值对'老男孩'，'linux'
# 4.将oldboy对应的字典中的alex对应的列表中的python2删除
dic1 = {
    'name':['alex',2,3,5],
    'job':'teacher',
    'oldboy':{'alex':['python1','python2','100']}
    }

print('1.将name对应的列表追加一个元素"wusir"')
dic1.get('name').append('wusir')
print(dic1)
print('2.将name对应的列表中的alex首字母大写。')
dic1['name'][0] = dic1.get('name')[0].capitalize()
print(dic1)
print('3.oldboy对应的字典加一个键值对"老男孩"，"linux"')
dic1.get('oldboy').setdefault('老男孩','linux')
print(dic1)
print('4.将oldboy对应的字典中的alex对应的列表中的python2删除')
dic1.get('oldboy').get('alex').remove('python2')
print(dic1)

