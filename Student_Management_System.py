import os

FILENAME = "students_data.txt"
if not os.path.exists(FILENAME):
    open(FILENAME, "w").close()

class Student:
    def __init__(self, name, sid, dept, year, marks):
        self.name = name
        self.sid = sid
        self.dept = dept
        self.year = year
        self.marks = marks

    def save(self):
        with open(FILENAME, "a") as f:
            f.write(f"{self.sid},{self.name},{self.dept},{self.year},{self.marks}\n")

def view_all():
    with open(FILENAME, "r") as f:
        print("\nID  Name  Dept  Year  Marks")
        for line in f:
            print(line.strip())

def search_student(sid):
    with open(FILENAME, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == str(sid):
                print("Found:", data)
                return
    print("Student not found")

def delete_student(sid):
    lines = []
    found = False
    with open(FILENAME, "r") as f:
        lines = f.readlines()

    with open(FILENAME, "w") as f:
        for line in lines:
            if line.split(",")[0] != str(sid):
                f.write(line)
            else:
                found = True
    print("Deleted" if found else "Student not found")

print("\n** Student Management System **")

while True:
    print("\n1.Add  2.View  3.Search  4.Delete  5.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        n = input("Name: ")
        i = int(input("ID: "))
        d = input("Department: ")
        y = input("Year: ")
        m = int(input("Marks: "))
        Student(n, i, d, y, m).save()

    elif ch == 2:
        view_all()

    elif ch == 3:
        sid = int(input("Enter ID: "))
        search_student(sid)

    elif ch == 4:
        sid = int(input("Enter ID: "))
        delete_student(sid)

    elif ch == 5:
        break
