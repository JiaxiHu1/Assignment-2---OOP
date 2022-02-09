import random


class Insect:
  
    def __init__(self):
        self.wings = 2
        self.legs = 4 
        self.distance = 0 


    def toss(self):
        self.distance = random.randint(1, 10)
     

    def get_distance(self):
            return self.distance
