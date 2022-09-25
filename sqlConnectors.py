import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="Testing",
    passwd="Chandran@12345",
    database="mark_register"
)
mycursor=db.cursor()

def check_password(id,password):

    mycursor.execute(f"SELECT UserID,TeacherID,Class FROM teachers WHERE Pass='{password}'")
    for i in mycursor:
        if i[0]==id:
            return (i[1], True, i[2])
    else:
        return (0, False, 0)




def session_info(id):
    mycursor.execute(f"SELECT UserID,MailID,Class,UniqueID FROM teachers WHERE TeacherID={id}")
    for i in mycursor:
        return i

# DUD METHOD DUE TO CHANGE VERY SHORTLY
def get_tests():
    return ("Pre-MidTerm","MidTerm","Quatery","HalfYearly","MidTerm-2","MidTerm-3","Revision-1","Revision-2")

'''mycursor.execute("SELECT * FROM teachers")
for i in mycursor:
    print(i)'''