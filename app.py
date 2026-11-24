students = []
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course name: ")
    student = {
        "name": name,
        "age": age,
        "course": course
    }
    students.append(student)
    print("Student added successfully!")
def view_students():
    if not students:
        print("No students found.")
        return
    for student in students:
        print(student)
add_student()
view_students()
