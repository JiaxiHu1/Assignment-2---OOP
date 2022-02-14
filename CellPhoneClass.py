#__manufacture attribute 
#__model attribute 
#__retail_price is the price of the retail price 

#__init__ method accept those three atrribute 

#3 other methods 
#set_manufacture 
#set_model 
#set_retail_price 

#3 gets to return the values 
import random 

class CellPhone: 
    def __init__(ma,mo,p):
        self.__manufacture = ma
        self.__model = mo
        self.__retail_price = p 
    
    def set_manufacture(ma): 
        ma = input("Enter the manufacture name:")
    

    def set_model(mo):
        mo = input("Enter the model:")

    
    def set_retail_price(p):
        p = float(input("Enter the retail price:"))
    

    def get_manufacture(self):
        return self.__manufacture 
    

    def get_model(self):
        return self.__model

    
    def get_retail_price(self):
        return self.__retail_price 

