import CellPhoneClass as cp 


manufacture =  input('Please enter the name of the manufacturer: ')
model =  input('Please enter the name of the model: ')
price = float(input('Please enter the retail price: ')) 

#when call we have to call the 
# this file was imported from .class 
#-- which file is it from and which class is it from 

cell = cp.CellPhone(manufacture,model,price)


print("the manufacture for the phone is", cell.get_manufacture())
print("the model of the phone is",cell.get_model())
print("the price for the phone is $", cell.get_retail_price())

