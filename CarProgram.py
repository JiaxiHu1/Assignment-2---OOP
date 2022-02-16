import CarClass as c 

yr = int(input("Please input the car's year model:"))

mk = input("Please input the make of the car:")

s = float(input("Please input the speed of the car:"))


my_speed = c.car(yr,mk,s)

for s in range(5): 
    my_speed.accelerate(s)
    print("The accelerate speed will be:",my_speed.get_speed(s))

for s in range(5):
    my_speed.brake(s)
    print("The brake mode speed will be:",my_speed.get_speed(s))

