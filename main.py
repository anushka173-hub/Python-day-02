
from assignment_c import Employee
from assignment_d import EmployeeRepository


repository = EmployeeRepository()

employee1 = Employee(1,
             "Aimila",
             "Nimal@gmail.com",
             30000,
             "it",
             "Active"
          )
     
employee2 = Employee(2,
                  "Isira",
                  "Isira@gmail.com",
                   70000,
                  "it",
               
                  "Active"
                  )
repository.create (employee1)
     
repository.create (employee2)

print(repository.get_all())

print(repository.get_by_id(1).get_details())

repository.update(1,34000)
repository.delete(2)

print(repository.get_all())


#------- HARD SCENARIO ---------

# # Client / Freontend
#         |
# # Routes/ Controller - Handle API request and responses. 
#         |
# # Validation - Check input data.
#         |
# # BUsiness Logic/Service - Handle Business rules.
#         |
# # repository - Handle database operations.
#         |
# # Database - Store data.

     

        
     

         
    

                   


     
     
                    


    
                 

     
         
     
        
          
        