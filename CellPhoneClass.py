#__manufacture attribute 
#__model attribute 
#__retail_price is the price of the retail price 

#__init__ method accept those three atrribute 

#3 other methods 
#set_manufacture 
#set_model 
#set_retail_price 

#3 gets to return the values 

class CellPhone: 
    #attributes will be defined with the __init__
    #every method is another define 
    def __init__(self,ma,mo,p):
        self.__manufacture = ma
        self.__model = mo
        self.__retail_price = p 
    
    def set_manufacture(self,ma):
        self.__manufacture = ma 
    
    def set_model(self,mo):
        self.__model = mo 
    
    def set_price(self,p):
        self.__price = p 

    def get_manufacture(self):
        return self.__manufacture 
    

    def get_model(self):
        return self.__model

    
    def get_retail_price(self):
        return self.__retail_price 

