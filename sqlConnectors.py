import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="Testing",
    passwd="root@12345",
    database="mark_register"
)
mycursor=db.cursor()

def check_password(id,password):
    user=''
    tid=0
    cls=''
    mycursor.execute(f"SELECT UserID,TeacherID,Class FROM teachers WHERE Pass='{password}'")
    for i in mycursor:
        user=i[0]
        tid=i[1]
        cls=i[2]
    if user==id:
        return (tid,True,cls)
    else:
        return (tid,False,cls)

def session_info(id):
    mycursor.execute(f"SELECT UserID,MailID,Class,UniqueID FROM teachers WHERE TeacherID={id}")
    for i in mycursor:
        return i


'''mycursor.execute("SELECT * FROM teachers")
for i in mycursor:
    print(i)'''