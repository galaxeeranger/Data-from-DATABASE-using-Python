"""We can Use both to connect with MySQL using pymysql and mysql.connector"""

import pymysql
# import mysql.connector
mydb = pymysql.connect(host = 'localhost',user = 'root',password = 'shiv')
# mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = 'shiv')

print(mydb)
"""Output: <pymysql.connections.Connection object at 0x000001BF4E7C12D0>"""

# mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = 'shiv',database = 'py_db')
mydb = pymysql.connect(host = 'localhost',user = 'root',password = 'shiv',database = 'py_db')

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor : 
    print("DataBases",x)

"""Output : 
DataBases ('information_schema',)
DataBases ('mysql',)
DataBases ('performance_schema',)
DataBases ('py_db',)
DataBases ('sakila',)
DataBases ('sys',)
DataBases ('world',)"""

mycursor = mydb.cursor()

mycursor.execute("USE py_db")
print("Using Database (py_db)")
"""Output:
Using Database (py_db)"""

mycursor.execute("SHOW TABLES")
for i in mycursor:
    print("Table Name",i)
"""Output:
Table Name ('student',)
Table Name ('teacher',)"""

mycursor.execute("SELECT * FROM student")
for x in mycursor :
    print("Student Data",x)
"""Output :
Student Data (1, 'Rohan', 'kamal@gmail.com', 1)
Student Data (2, 'Rahul', 'rahul@gmail.com', 1)
Student Data (3, 'Roy', 'roy@gmail.com', 2)"""

mycursor.execute("SELECT * FROM teacher")
for x in mycursor :
    print("Teacher Data",x)
"""Output :
Teacher Data (1, 'Kamal', 'kamal@gmail.com', '9889876545')
Teacher Data (2, 'Nandan', 'nandan@gmail.com', '9876789876')
Teacher Data (3, 'Harendra', 'hari@gmail.com', '9876789876')"""

mycursor.execute("SELECT * FROM student WHERE TEACHER_ID =1")
for s in mycursor :
    print("Student Data with TEACHER id : 1",s)
"""Output:
Student Data with TEACHER id : 1 (1, 'Rohan', 'kamal@gmail.com', 1)
Student Data with TEACHER id : 1 (2, 'Rahul', 'rahul@gmail.com', 1)"""

# sql="SELECT * FROM student INNER JOIN teacher ON student.teacher_id=teacher.id"
sql = "SELECT * FROM student INNER JOIN teacher ON student.teacher_id = teacher.id WHERE teacher.id IS NOT NULL"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
"""Output:
(2, 'Rahul', 'rahul@gmail.com', 1, 1, 'Kamal', 'kamal@gmail.com', '9889876545')
(1, 'Rohan', 'kamal@gmail.com', 1, 1, 'Kamal', 'kamal@gmail.com', '9889876545')
(3, 'Roy', 'roy@gmail.com', 2, 2, 'Nandan', 'nandan@gmail.com', '9876789876')"""

import json

sql = "SELECT * FROM teacher INNER JOIN student ON student.teacher_id = teacher.id"

mycursor.execute(sql)
myresult = mycursor.fetchall()
result_list = []
for row in myresult:
    result_dict = {}
    result_dict['teacher_id'] = row[0]
    result_dict['teacher_name'] = row[1]
    result_dict['teacher_email'] = row[2]
    result_dict['teacher_phone'] = row[3]
    result_dict['student_id'] = row[4]
    result_dict['student_name'] = row[5]
    result_dict['student_email'] = row[6]
    result_dict['teacher_id_key'] = row[7]
    result_list.append(result_dict)

json_data = json.dumps(result_list)
print(json_data)
"""Output:
[{"teacher_id": 1, "teacher_name": "Kamal", "teacher_email": "kamal@gmail.com", "teacher_phone": "9889876545", 
"student_id": 1, "student_name": "Rohan", "student_email": "kamal@gmail.com", "teacher_id_key": 1}, 

{"teacher_id": 1, "teacher_name": "Kamal", "teacher_email": "kamal@gmail.com", "teacher_phone": "9889876545", 
"student_id": 2, "student_name": "Rahul", "student_email": "rahul@gmail.com", "teacher_id_key": 1}, 

{"teacher_id": 2, "teacher_name": "Nandan", "teacher_email": "nandan@gmail.com", "teacher_phone": "9876789876", 
"student_id": 3, "student_name": "Roy", "student_email": "roy@gmail.com", "teacher_id_key": 2}]"""
