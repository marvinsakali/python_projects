from students import Students


class University:
    def __init__(self):
        self.students = {}
        self.courses = ["CSC101", "MTH101", "GIS201"]

    def add_student(self, student):
        if student.get_id in self.students:
            print("Student already exists")
        else:
            self.students[student.get_id] = student
            print("Student added successfuly!")

    def view_students(self):
        for i, (key, student) in enumerate(self.students.items()):
            if len(key) == 0:
                return
            else:
                print(f"{i+1}. {key} --> {student.full_name}")

    def remove_student(self, student):
        self.view_students
        if student in self.students:
            del self.students[student]
            print('Student removed successfully')
        else:
            print("Student does not exist!")

    def register_to_units(self, student_reg, course_id):
        if course_id in self.courses:
            if student_reg in self.students:
                student = self.students[student_reg]
                student.register_course(course_id)
                print('Course registered successfuly!')
            else:
                print("Student does not exist")
        else:
            print("Unit does not exist!")

    def display_student(self, student_reg):
        if student_reg in self.students:
            print('Student available')
            self.students[student_reg].display_info
        else:
            print("No such student!")
