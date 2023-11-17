# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='employee'
# )
# mycursor=mydb.cursor()
# sql="select * from details"   #* is universal symbol used to select all data
# mycursor.execute(sql)
# a=mycursor.fetchall()
# # print(a)                #we get only complete tuple   so we use element accessing
# # for i in a:
# #     print(i)    #here we return tuple in line byline   if we need seperately we use element accessing
#
# for i in a:
#     id=i[0]
#     name=i[1]
#     email=i[2]
#     phone_number=i[3]
#     print("id=",id,"name=",name,"email=",email,"phone number=",phone_number)


# fetching product details
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# sql='select * from product_details'
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     id=i[0]
#     name=i[1]
#     price=i[2]
#     cutomer_name=i[3]
#     phone_number=i[4]
#     print("id=",id,"name=",name,"price=",price,"customer name=",cutomer_name,"phone number=",phone_number)
