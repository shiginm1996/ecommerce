# delete row using id

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='employee'
# )
# mycursor=mydb.cursor()
# id=int(input('enter the id to delete'))
# sql='delete from details where id=%d'%id
# mycursor.execute(sql)
# mydb.commit()
# print('row deleted')

# Q1. delete using product name and customer name
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# name=input('enter product name')
# cusname=input('enter customer name')
# sql='delete from product_details where name="%s" and cutomer_name="%s"'%(name,cusname)
# mycursor.execute(sql)
# mydb.commit()
# print('data deleted successfully')


# if both the condition needs to fulfill otherwise return not found
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# nm=input('enter the product name')
# cusnm=input('enter the customer name')
# sql="select name,cutomer_name from product_details"
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     if nm==i[0] and cusnm==i[1]:
#         sql1='delete from product_details where name="%s" and cutomer_name="%s"'%(nm,cusnm)
#         mycursor.execute(sql1)
#         mydb.commit()
#         print('success')
#         break
# else:
#     print('data not found')