class Employee:
    Name = ""
    Age = 18
    Dept = ""
    Manager = ""
    Salary = 0

    def __init__(self,Name, Age, Dept, Manager_n, Salary):
        self.Name = Name
        self.Age = Age
        self.Dept = Dept
        self.Manager = Manager_n
        self.Salary = Salary

    def get_salary(self, Compensation):
        print(f"Total Salary of employee {self.Name} is {self.Salary + Compensation}")


class Manager(Employee):
    TA = 1000 # travel allowance
    RA = 15000  # rent allowance

    # overridden method
    def get_salary(self, Compensation):
        print(f"Total salary of manager {self.Name} is {self.Salary + Compensation + self.TA + self.RA}")


emp1 = Employee("Dev Nakum", 20, "CE", "Henil Mistry", 25000)
manager1 = Manager("Henil Mistry", 20, "CE", "", 50000)

emp1.get_salary(10000)
manager1.get_salary(10000)
