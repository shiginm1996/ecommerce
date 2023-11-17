# Q1.write a python function that takes a list of words as argument and returns the longest word and length of the longest word

print('Question.1')
li=['babu','suresh','rakesh','sureshkumar']
def longest(li):
    longest_word=''
    length=0
    for i in li:
        if len(i)>length:
            longest_word=i
            length=len(i)
    print('longest word=',longest_word)
    print('length of the word=',length)
longest(li)


# # Q2.write a python programme to remove charectors that have odd index value in the given string
print('Question.2')
word=input('enter the word')
st=''
for i in word:
    if word.index(i)%2==0:
        st+=i
print(st)
#
# Q3.iterate a list and print a new dictionary with the element and its index positioning
print('Question.3')

li=['a','b','c','d']
dic={}
for i in li:
    key=i
    value=li.index(i)
    dic.update({key:value})
print(dic)

# Q4.iterate a tuple of a number and find the sum of each digit and generate a new tuple
print('question 4')
print('t=(123,235,478)')
num = (123,235,478)
new = ()

for number in num:
    n= str(number)
    s = sum(int(digit) for digit in n)
    new += (s,)
print('sum of digit=',new)
#
#
# # Q5.write a programme to swap the first and last letter of the string and generate a new string
print('Question.5')
word="hello"
first=word[0]
last=word[-1]
mid=word[1:-1]
new_str=last+mid+first
print(new_str)













