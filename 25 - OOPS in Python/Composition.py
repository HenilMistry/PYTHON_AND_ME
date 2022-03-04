# student class...
class Student:
    # constructor method..
    def __init__(self, id):
        self._id = id

    def registration_number(self, department_id) -> str:
        return str(self._id) + '-' + department_id


# department class..
class Department:
    # constructor of class...
    def __init__(self, department_id, student_id):
        self._id = department_id
        self._student = Student(student_id)  # making a student object...

    def student_registration(self):
        return self._student.registration_number(self._id)


if __name__ == '__main__':
    department = Department('ENG', 10)
    print(department.student_registration())