# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# limit=int(input('enter the limit'))
# sql="select * from product_details limit %d"%limit
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     id=i[0]
#     name=i[1]
#     price=i[2]
#     cutomer_name=i[3]
#     phone_number=i[4]
#     print('id=',id,'name=',name,'price=',price,'customer name=',cutomer_name,'phone number=',phone_number)

# same product name have more data but we wants to dispaly only 2 data use limit with condition
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# productnm=input('enter name')
# limit=int(input('enter limit'))
# sql='select * from product_details where name="%s" limit %d'%(productnm,limit)
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     id=i[0]
#     name=i[1]
#     price=i[2]
#     cutomer_name=i[3]
#     phone_number=i[4]
#     print('id=',id,'name=',name,'price=',price,'cutomer name=',cutomer_name,'phone number=',phone_number)


# min and max(price,id)

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# sql='select min(price) from product_details'
# mycursor.execute(sql)
# a=mycursor.fetchone()
# print(a[0])

# max
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# sql='select max(price) from product_details'
# mycursor.execute(sql)
# a=mycursor.fetchone()
# print(a[0])

# min and max
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# sql='select max(price),min(price) from product_details'
# mycursor.execute(sql)
# a=mycursor.fetchone()
# print('max=',a[0])
# print('min=',a[1])


#average
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# sql='select avg(price) from product_details'
# mycursor.execute(sql)
# a=mycursor.fetchone()
# print('avg=',a[0])


