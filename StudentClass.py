#Create a method that calculate the students' current age and display on the screen 
#create a method that will tell the user when the student can register 
#Senior 11/1-11/3
#Junior 11/4-11/6
#Sophomores 11/7-11/9 
#Freshman 11/10-11/12

from datetime import date 

class Student:
    def __init__(self):
        self.age = 0 
    
    def age(birthdate):
        today = date.today()
        age = today.year - birthdate.year - ((today.month.today.day)) < (birthdate.month,birthdate.day)
        return age
    
    def get_age(self):
        return self.age 
