class Students:
    def __init__(self, first, middle, last, reg_no, program, year):
        self.__first = first
        self.__middle = middle
        self.__last = last
        self.__reg_no = reg_no
        self.__program = program
        self.__year = year
        self.__course = []

    @property
    def full_name(self):
        return "{} {} {}".format(self.__first, self.__middle, self.__last)

    @full_name.setter
    def full_name(self, name):
        first, middle, last = name.split(" ")
        self.first = first
        self.middle = middle
        self.last = last

    @property
    def email(self):
        return "{}.{}@student.jkuat.ac.ke".format(self.__last, self.__middle)
    
    def register_course(self, course):
        if course not in self.__course:
            self.__course.append(course)

    @property
    def display_info(self):
        print("\n --- Student Info ---")
        print(f"Name: {self.full_name}")
        print(f"Reg no: {self.__reg_no}")
        print(f"Email: {self.email}")
        print(f"Program: {self.__program}")
        print(f"Year: {self.__year}")
        if not self.__course:
            return 
        else:
            for course in self.__course:
                print(f"Units: {course}")

    @property
    def get_id(self):
        return self.__reg_no


student_1 = Students('Marvin', "Sakali", 'Ogajo', 'enc-222-0154', 'Gis', '4')
# student_1.display_info
print(student_1.get_id)
