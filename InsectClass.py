import random


class Insect:
  
  #add w and l to the title will let the users make changes 
  #error will occur - that 2 required positional argument w and l are not assigned value 
  
    def __init__(self,w,l):
        self.wings = w 
        self.legs = l 
        self.flight = 0 

#make each method only do one thing 
#we assign the flight distance is a random number from 1-10 
    def flight_length(self):
        self.flight = random.randint(1, 10)
     
#and then we return the miles of the flight 
    def get_miles(self):
            return self.flight
