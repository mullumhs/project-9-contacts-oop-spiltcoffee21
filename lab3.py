"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Enhance the Contact class by adding instance and class methods.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Copy/paste your Contact class from Lab 2.
# 2. Add a check_email method to check if the email contains an '@'
# 3. Create a class method get_contact_count to retrieve the number of contacts
# 4. Reproduce the instances of the Contact class that you created in Lab 2
# 5. Call your new instance method on one Contact and print the result
# 6. Use the class method to print out the total number of contactsclass Contact:
class Contact:
    number_of_contact = 0
    
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        Contact.number_of_contact += 1

    def check_email(self):
        if "@" in self.email:
            print("yes")
            return True
        else:
            print("no")
            return True

@classmethod
def get_contact_count(cls):
        
    return Contact.number_of_contact 


contact1 = Contact("remy", "04568239454", "remy.ross.morrow@gmail.com")
contact2 = Contact("rocco jr", "045738274", "rocco.jr@gmail.com")

contact1.check_email()