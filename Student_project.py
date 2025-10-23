class Student: #class
    #class attributes
    school = "Bengazy"

    #constructor
    def __init__(self, name, age, student_id, subject, exam_grade, project_grade):
        #Instance attributes/variables
        self.name = name
        self.age = age
        self.student_id = student_id
        self.subject = subject
        self.exam_grade = exam_grade
        self.project_grade = project_grade

    #display student details
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Subject: {self.subject}")
        print(f"Exam Grade: {self.exam_grade}")
        print(f"Project Grade: {self.project_grade}")

    #calculate_average
    def calculate_average(self):
        cal_average = (self.exam_grade + self.project_grade) / 2
        return cal_average

    def update_grade(self, exam_grade, project_grade):
        self.exam_grade = exam_grade
        self.project_grade = project_grade
        self.display_info()

#Object Creation
student1 = Student(name="Trump",age=28,student_id=9055,
                   subject="Statistics",exam_grade=77,
                   project_grade=80)

student1.display_info()
student2 = Student("ben",12,96654, "maths", 90, 67)
student2.display_info()
print("-----------------")
print(student2.calculate_average())
print("-----------------")
print(student1.calculate_average())
