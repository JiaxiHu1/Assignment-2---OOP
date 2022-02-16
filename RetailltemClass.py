class Retailltem: 
    def __init__(self,des,inv,p):
        self.__description = des 
        self.__inventory = inv 
        self.__price = p 
    

    def get_description(self):
        return self.__description
    
    def get_inventory(self):
        return self.__inventory 
    
    def get__price(self):
        return self.__price 
