# Assignment D


class EmployeeRepository:

     def __init__(self):
          self.employee = []

     def create (self , employee):
          self.employee.append (employee)
          return employee

     def get_by_id(self, employee_id) :
          for employee in self.employee:
               if employee.employee_id == employee_id:
                    return employee
               return None
          
     def get_all(self):
               return self.employee

          
     def update(self,employee_id,new_salary):
      employee = self.get_by_id(employee_id)
      if employee: employee.update_salary(new_salary)
      return employee
      return None

     def delete(self,employee_id):
          employee = self.get_by_id(employee_id)
          if employee:
               self.employee.remove(employee)
               return True
          return False