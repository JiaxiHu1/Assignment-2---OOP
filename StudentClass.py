#Create a method that calculate the students' current age and display on the screen 
#create a method that will tell the user when the student can register 
#Senior 11/1-11/3
#Junior 11/4-11/6
#Sophomores 11/7-11/9 
#Freshman 11/10-11/12

from datetime import date 

class Student:
    def __init__(self,dob,classi):
        self.__dob = dob 
        self.__classification = classi 
        self.__registration = ""
        self.__age = 0
    
    #age 
    def age(self):
        today = date.today()
        dob = self.__dob.split('/')
        dob_yr = int(dob[2])
        age = today.year - dob_yr
        self.__age = age 
    
    def get_age(self):
        return self.__age 

    #registration time 
    def reg_time(self):
        if self.__classification == 'Senior':
            self.__registration = '11/1 thru 11/3'
        elif self.__classification == 'Junior':
            self.__registration = '11/4 thru 11/6'
        elif self.__classification == 'Sophomore':
            self.__registration = '11/7 thru 11/9'
        elif self.__classification == 'Freshman':
            self.__registration = '11/10 thru 11/12'
        else:
            self.__registration = 'Please Enter Another Classification.'

    def get_reg_time(self):
        return self.__registration