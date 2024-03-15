import psycopg2

# connecting to database, and conn is now the object used to talk with db
conn = psycopg2.connect(database="postgres",
                            host="localhost",
                            user="victor",
                            password="admin",
                            port="5432")
cursor = conn.cursor()


# prints all rows in Students table
def getAllStudents():
    cursor.execute("SELECT * FROM Students")
    print(cursor.fetchall())

# prints newly added student in Students table, and adds to table in postgresql
def addStudent(first_name, last_name, email, enrollment_date):
    cursor.execute(f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES('{first_name}', '{last_name}', '{email}', '{enrollment_date}');")
    print(f"added {first_name} {last_name} to Students")

# updates existing student email with new_email and prints the student id with new email
def updateStudentEmail(student_id, new_email):
    cursor.execute(f"UPDATE Students SET email = '{new_email}' WHERE student_id = '{student_id}'")
    print(f"set {student_id} email to {new_email}")

# deletes student_id from Students table
def deleteStudent(student_id):
    cursor.execute(f"DELETE FROM Students WHERE student_id='{student_id}'")
    print(f"deleted {student_id}")


# deleteStudent(1)
getAllStudents()
# addStudent("Victoria", "Sandra", "email@gmail.com", "2023-01-05")
# getAllStudents()
# updateStudentEmail("10", "victoria@gmail.com")
deleteStudent("10")
getAllStudents()
conn.commit()
