# for i in range(10):
#     print('hello')
# num=int(input('enter a number'))
# for i in range(num):
#     print('hello')
# for i in range(11):
#     print(i)
# num=int(input('enter a number'))
# for i in range(num+1):
#     print(i)
# for i in range(1,11):
#     print(i)
# initial=int(input('enter initial value'))
# final=int(input('enter final value'))
# for i in range(initial,(final+1)):
#     print(i)
# for i in range(1,10):
#     if i%2==0:
#         print(i)
# for i in range(1,10):
#     if i%2!=0:
#         print(i)
# a=int(input('enter inital'))
# b=int(input('enter final'))
# for i in range(a,(b+1)):
#     if i%2==0:
#         print(i)
sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)
# sum=0
# for i in range(2,21):
#     if i%2==0:
#         sum+=i
# print(sum)
# product=1
# for i in range(1,11):
#         product*=i
# print(product)
# sum=0
# sum1=0
# for i in range(100,200):
#     if i%2==0:
#         sum+=i
#     else:
#         sum1+=i
# print(sum)
# print(sum1)
# num=int(input('enter a number'))
# for i in range(1,11):
#     print('%d * %d = %d'%(num,i,(num*i)))
# product=1
# a=int(input('enter a number'))
# for i in range(1,a+1):
#     product*=i
# print('factorial of %d is %d'%(a,product))
#20-04-2023
# for i in range(2,11,2):
#
#     print(i)
# for i in range(1,20,2):
#     print(i)
# for i in range(5,31,5):
#     print(i)
# for i in range(10,0,-1):
#     print(i)
# for i in range(100,0,-1):
#     print(i)
# for i in range(5000,900,-1000):
#     print(i)
# s=0
# s1=0
# for i in range(12,38):
#     if i%2==0:
#         s+=i
#     else:
#         s1+=i
# print(s)
# print(s1)
# for i in range(100,500):
#     if i%11==0 and i%2!=0:
#         print(i)


# n=int(input('enter a number'))
# for i in range(97,97+n):
#     for j in range(97,i+1):
#         print(chr(i),end=' ')
#     print()


# n=int(input('enter a number'))
# for i in range(96+n,96,-1):
#     for j in range(97,i+1):
#         print(chr(i),end=' ')
#
#     print()

#
n=int(input('enter a number'))
for i in range(97,97+n):#i=97,98,99
    for j in range(100,i,-1):
        print(chr(i),end=' ')
    print()








