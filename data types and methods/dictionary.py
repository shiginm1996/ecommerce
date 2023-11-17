# 03-05-23
# person={
#     'name':'shigin',
#     100:200,
#     'address':'kannur',
#     'phone':9747806171
#
# }
# print(person)
# print(type(person))
# print(person.keys())
# print(person.values())
# print(person.get('name'))
# without function
# a=person['name']
# print(a)
# a=input('enter the key')
# print(person.get(a))
# length of dictionary
# print(len(person))
# person.update({'age':27})
# print(person)
# updating existing
# person.update({'address':'thalora'})
# print(person)
# user input updation
# key=input('enter the key')
# values=input('enter the value')
# if key.isdigit:
#     print(person.update({key:int(values)}))
# else:
#     print(person.update({key:values}))
#
# print(person)
# without using function updation
# person['age']=27
# print(person)
# pop
# person.pop('phone')
# print(person)
# person.popitem()
# print(person)
# dictionary iteration
# only keys
# for i in person:
#     print(i)
# only values
# for i in person.values():

#     print(i)
# both
# for i,j in person.items():
#     print(i,j)
dic={}
n=int(input('enter number of keys'))
for i in range(n):
    key=input('enter key')
    value=input('enter value')
    if value.isdigit():
        dic.update({key:int(value)})
    elif '.' in value:
        dic.update({key:float(value)})
    else:
        dic.update({key:value})
print(dic)
