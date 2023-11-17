# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='employee'
# )
# mycursor=mydb.cursor()
# id=int(input('enter the id'))
# sql="select * from details where id=%d"%id
# mycursor.execute(sql)
# a=mycursor.fetchone()    # no iteration bcz only single tuple is there in a
# id=a[0]
# name=a[1]
# email=a[2]
# phone_number=a[3]
# print("id=",id,"name=",name,"email=",email,"phone number=",phone_number)

# product table fetchdata using name,print product name and price

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# name=input('enter product name')
# sql="select * from product_details where name='%s'"%name
# mycursor.execute(sql)
# a=mycursor.fetchone()
# name=a[1]
# price=a[2]
# print("product name=",name,"price=",price)





# Q.prod name,price,customer name   without using *
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# sql='select name,price,cutomer_name from product_details'
# mycursor.execute(sql)
# a=mycursor.fetchall()
#
# for i in a:
#     name=i[0]
#     price=i[1]
#     cutomer_name=i[2]
#     print('name=',name,'price=',price,'customer name=',cutomer_name)

