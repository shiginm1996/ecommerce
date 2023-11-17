# import re
# str='this is my paragraph'
# pattern=input('enter the word')
# x=re.findall(pattern,str)
# print(x)


# import re
# str='this is my paragraph'
# pattern='^[a-z]+'
# x=re.findall(pattern,str)
# print(x)

# import re
# str='my first number is 12456 and my second number is 2345'
# pattern='\d+'            #equals to [0-9]+
# x=re.findall(pattern,str)
# print(x)
#
# import re
# str='my first number is 12456 and my second number is 2345'
# pattern='\D+'            #equals to [0-9]+
# x=re.findall(pattern,str)
# print(x)
#
# import re
# str='my first number is 12456 and my second number is 2345'
# pattern='\w+'            #equals to [0-9]+
# x=re.findall(pattern,str)
# print(x)


# search     returns object location
# import re
# str='hello world'
# word=input('enter a word')
# x=re.search(word,str)    #only one object
# print(x)

# import re
# str='hello world'
# pattern='\s+'
# x=re.search(pattern,str)    #only one object
# print(x)
#
# import re
# str='hello world'
# pattern='\d+'
# x=re.search(pattern,str)    #only one object
# print(x)
#
# import re
# str='hello world'
# pattern='\w+'
# x=re.search(pattern,str)    #only one object
# print(x)



# 07-06-2023
# split ()

# import re
# txt='arun and abhi are students'
# x=re.split(' ',txt)
# print(x)

# import re
# url='static/images/projectfile/image.png'
# x=re.split('/',url)    #   if \   r will put before it
# print(x[-1])

# using \
# import re
# url=r'static\images\projectfile\image.png'    #r is used to avoid unicode error
# x=re.split(r'\\',url)    #   if \   r will put before it
# print(x[-1])

# import re
# txt='arun and abhi are friends'
# x=re.split('\s',txt,1)
# y=re.split('\s',txt,2)
# z=re.split('\s',txt,3)
# print(x)
# print(y)
# print(z)


# sub()
# import re
# a='hello welcome to python'
# x=re.sub('\s','#',a,1)
# y=re.sub('\s','#',a,2)
# print(x)
# print(y)