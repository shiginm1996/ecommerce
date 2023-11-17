# import re
# rule="[A-Za-z]+"
# word=input("enter your name")
# match=re.fullmatch(rule,word)
# if match:
#     print('valid name')
# else:
#     print('invalid name')

# rule:
# name should start with upper case
# lower case,space
# 7,10 including space
# import re
# rule="^[A-Z][a-z\s]{6,9}"    #bcz already one from first rule^[AZ] balance min=6 and max 9
# word=input('enter a word')
# match=re.fullmatch(rule,word)
# if match:
#     print('valid word')
# else:
#     print('invalid word')


# rule
# the name should only start with upper A,B or C
# followed by lower case
# number shouldbe included or not included
# import re
# rule='^[ABC][a-z]+[0-9]*'
# word=input('enter a word')
# match=re.fullmatch(rule,word)
# if match:
#     print('valid word')
# else:
#     print('invalid word')


# 05-06-2023
# phone number validation
# 10 numbers required
# it should start with 9,8,7,6

# import re
# rule='^[9876][0-9]{9}'
# num=input('enter a number')      #bcz taken as string
# match=re.fullmatch(rule,num)
# if match:
#     print('valid number')
# else:
#     print('invalid number')

# +91
# starts with 9876
# numbers limit except +91 is 10

# import re
# rule='^[+][9][1][6-9][0-9]{9}'               #6-9 or 9876
# num=input('enter number')
# match=re.fullmatch(rule,num)
# if match:
#     print('valid number')
# else:
#     print('invalid number')

# Q.
# 1.The name should only starts with upper cas A,B,or C
# 2.Followed by lower case
# 3. number should be included or not included

# import re
# rule='^[ABC][a-z]+([0-9]{1,2}|[^0-9])'        #here [0-9]* is not given bcz we we can give only 2 * means not or give any number of values
# word=input('enter word')
# match=re.fullmatch(rule,word)
# if match:
#     print('valid word')
# else:
#     print('invalid word')



# Email validation

# Q
# 1.shigin@gmail.com
# 2.shigin123456..@gmail.com
# 3.shigin_123456...@gmail.com   spcl char _,* if there at once
# 4.123@gmail.com not valid

# import re
# rule='^[a-z]+[0-9]*[*_]?[a-z0-9]*@gmail.com'
# mail=input('enter mailid')
# match=re.fullmatch(rule,mail)
# if match:
#     print('valid mail')
# else:
#     print('invalid mail')

# 06-05-2023
# registration and login using regex
# enter  name
# enter email
# enter phone number
# enter password
# if four condition true reg success
# else registration failed
# login page:
# email
# password
# login success or login failed
# import re
# name=input('enter your name')
# email=input('enter your email')
# phnno=input('enter your phone number')
# password=input('enter your password')
# rule1='[A-Za-z]+'
# rule2='^[a-z]+[0-9]*[*_]?[a-z0-9]*[@][g][m][a][i][l][.][c][o][m]'
# rule3='^[9876][0-9]{9}'
# rule4='[A-Za-z0-9]+{4,8}'
# match1=re.fullmatch(name,rule1)
# match2=re.fullmatch(email,rule2)
# match3=re.fullmatch(phnno,rule3)
# match4=re.fullmatch(password,rule4)
# if match1 and match2 and match3 and match4:
#     print('Registration Success')
#     print('Login Page')
#     id=input('enter your email')
#     pw=input('enter your password')
#     if email==id and password==pw:
#         print('Login Success')
#     else:
#         print('Login unsuccessful')
# else:
#     print('Registration Failed')





import re
rule1='[A-Za-z]+'
rule2='^[a-z]+[0-9]*[*_]?[a-z0-9]*@gmail.com'
rule3='^[9876][0-9]{9}'
rule4='[A-Za-z0-9]{4,8}'
name=input('enter your name')
match1=re.fullmatch(rule1,name)
email=input('enter your email')
match2=re.fullmatch(rule2,email)
phnno=input('enter your phone number')
match3=re.fullmatch(rule3,phnno)
password=input('enter your password')
match4=re.fullmatch(rule4,password)
if match1 and match2 and match3 and match4:
    print('Registration Success')
    print('Login Page....')
    id=input('enter your email')
    pw=input('enter your password')
    if email==id and password==pw:
        print('Login Success')
    else:
        print('Login unsuccessful')
else:
    print('Registration Failed')

