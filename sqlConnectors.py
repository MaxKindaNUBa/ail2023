import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="Testing",
    passwd="Chandran@12345",
    database="mark_register"
)
mycursor = db.cursor()


def check_password(idd, password):
    mycursor.execute(f"SELECT UserID,TeacherID,Class FROM teachers WHERE Pass='{password}'")
    for i in mycursor:
        if i[0] == idd:
            return i[1], True, i[2]
    else:
        return (0, False, 0)


def session_info(idd):
    mycursor.execute(f"SELECT UserID,MailID,UniqueID FROM teachers WHERE TeacherID={idd}")
    for i in mycursor:
        return i


# DUD METHOD DUE TO CHANGE VERY SHORTLY
def get_tests():
    t = tuple()
    mycursor.execute("SELECT ExNAME FROM EXAMS ")
    for i in mycursor:
        t += i
    return t


def getStudentStats(clas: str):
    # returns bio,csc,english students
    t = tuple()
    mycursor.execute(f"select count(elective) from students where class='{clas}' group by elective order by elective")
    for i in mycursor:
        t += i
    return [f"BIO Students : {t[0]}", f"CSC Students : {t[1]}", f"EG Students : {t[2]}",
            f"\nTotal Students : {t[0] + t[1] + t[2]}"]


def get_student_list(clas):
    t = tuple()
    mycursor.execute(f"SELECT RollNO,StdName FROM STUDENTS WHERE Class='{clas}'")
    for i in mycursor:
        t += (f"{i[0]} : {i[1]}",)
    return t


def get_classes():
    l = tuple()
    mycursor.execute("SELECT distinct Class from students;")
    for i in mycursor:
        l += (i)
    return l


def get_table(clas, test):
    mycursor.execute(
        f"SELECT students.RollNO,StdName,students.Elective,Physics,Chemistry,Maths,English,{test}.Elective FROM "
        f"students,{test} where students.rollno={test}.rollno and class='{clas}';")
    return mycursor.fetchall()


def get_no_failed(clas, exam, subject="ALL"):
    roll = str(120 + ord(clas[3]) - 64)
    if subject == "ALL":
        mycursor.execute(
            f"select count(rollno) from {exam} where rollno like '{roll + '__'}' and (physics+chemistry+maths+english"
            f"+elective)<=200;")
    else:
        mycursor.execute(f"select count(rollno) from {exam} where rollno like '{roll + '__'}' and {subject}<=40;")
    for i in mycursor:
        return i[0]


def get_marks(clas, exam, subject="ALL"):
    roll = str(120 + ord(clas[3]) - 64)
    if subject == "ALL":
        mycursor.execute(
            f"select physics+chemistry+maths+english+elective from {exam} where rollno like '{roll + '__'}'")
    else:
        mycursor.execute(f"select {subject} from {exam} where rollno like '{roll + '__'}'")
    t = []
    for i in mycursor:
        t += i
    return t


def get_code(name):
    mycursor.execute(f"SELECT excode from exams where exname='{name}';")
    for i in mycursor:
        return i[0]


def get_date(exam):
    mycursor.execute(f"select exdate from exams where excode='{exam}';")
    for i in mycursor:
        return i[0].strftime('%d/%m/%Y')




# THESE 2 NOT WORKINGGGGG
def addExam(exname,exdate):
    n = len(get_tests())
    code=''
    for i in exname:
        if i.isalpha():
            code+=i.lower()
    mycursor.execute(f"insert into exams values({n+1},'{exname}','{exdate}','{code}');")
    db.commit()

def register_teacher(userid,password,mailid,clas,uniqueid):
    mycursor.execute("select count(*) from teachers")
    count= mycursor.fetchall()[0][0]
    mycursor.execute(f"insert into teachers(TeacherID,UserID,Pass,MailID,Class,UniqueID) values ({count+1},'{userid}','{password}','{mailid}','{clas}','{uniqueid}')")
    db.commit()
