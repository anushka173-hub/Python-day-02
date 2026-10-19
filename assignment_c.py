#Assignment C

class Employee:

    def __init__(self,employee_id,name,email,salary,department,status):
          if salary < 0 :
               raise ValueError ("Salary cannot be nagative")

          self.employee_id = employee_id 
          self.name = name
          self.email = email
          self.salary = salary
          self.department = department
          self.status = status

    def get_details(self):
          return {"employee ID":self.employee_id,
                  "name" : self.name,
                  "email" : self.email,
                  "salary": self.salary,
                  "department": self.department,
                  "satus": self.status
                  }
    def calculate_annual_salary(self):
          return  self.salary * 12

    def update_salary (self,new_salary):
          if new_salary < 0 :
               raise
          ValueError("salary cannot be nagative")

          self.salary = new_salary