from ORM_Trial.models import *


def add_student(name):
    while name is None:
        name = input("Enter student name:")
    session.add(Student(name))
    session.commit()


def main():
    students = Student().get_all()
    for i, student in enumerate(students):
        print(student.name)


if __name__ == '__main__':
    main()
