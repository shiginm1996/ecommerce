stk=[]
size=int(input('enter the size of stack:'))
top=0
def push():
    global top
    if top==size:
        print('stack is full')
    else:
        el=int(input('enter the element'))
        stk.append(el)
        top+=1
        print(stk)


def pop():
    global top
    if top==0:
        print('stack is empty')
    else:
        stk.pop()
        top-=1
        print(stk)
while True:
    print('operation to perform')
    choice=int(input('1.push\t\t2.pop:'))
    if choice==1:
        push()
    elif choice==2:
        pop()
    else:
        print('invalid input')

# 2.Queue
# queue=[]
# top=0
# size=int(input('enter the size of the stack'))
# def enqueue():
#     global top
#     if top==size:
#         print('queue is full')
#     else:
#         el=int(input('enter the element'))
#         queue.append(el)
#         top+=1
#         print(queue)
# def dequeue():
#     global top
#     if top==0:
#         print('queue is empty')
#     else:
#         queue.pop(0)
#         top-=1
#         print(queue)
# while True:
#     print('operation to perform')
#     choice=int(input('1.enqueue\t\t2.dequeue:'))
#     if choice==1:
#         enqueue()
#     elif choice==2:
#         dequeue()
#     else:
#         print('invalid input')
