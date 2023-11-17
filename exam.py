# # q1 write a python function that takes list of elements and argument and generate a new list which contains factorial of each elements
# # function with argument
#
# # Q2. print left angle riangle
#
# #       *
# #    *   *
# # *  *   *
#
# # Q3.{val1.1,val2:2,val3:3,val4:4,val5:5,val6:6}
# # from the above dic fetch keyvaluepairs that only have even values
#
# # Q4. ['a','a','b','b','c']
# # pass the above list in to a function and return a new list by removing duplicate values from the list
# # Q5. [1,2,3,4,5]from the list find min and max value from the list using function with return
#
#
# #ANSWERS
# # Q1.
# li=[1,2,3,4]
# lis=[]
# def fact(li):
#     f=1
#     for i in li:
#         f*=i
#         lis.append(f)
#     return(lis)
# print(fact(li))
#
# # Q2.
#
# for i in range(0,3):
#     for k in range(0,3-i-1):
#         print(' ',end=' ')
#     for j in range(0,i+1):
#             print('*',end=' ')
#     print()
#
# # Q3.
# dic={
#     'val1':1,
#     'val2':2,
#     'val3':3,
#     'val4':4,
#     'val5':5,
#     'val6':6
# }
# for j,i in dic.items():
#     if i%2==0:
#         print(j,i)
#
# # Q4.
# li=['a','a','b','b','c']
# x=set(li)
# print(list(x))
#
# li=['a','a','b','b','c']
# a=set(li)
# b=list(a)
# b.sort()
# print(b)
#
# # Q5.
# li=[1,2,3,4,5]
# def min(*a):
#     li.sort()
#     m=li[0]
#     return m
# def max(*a):
#     li.sort()
#     l=li[-1]
#     return l
# print('minimum value=',min())
# print('maximum value=',max())










