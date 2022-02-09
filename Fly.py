import InsectClass as i


def main():
       # Create an object from the Coin class.
       my_distance = i.Insect()   # this creates an instance called 'my_coin' of the class 'Coin()'

       # Display the side of the coin that is facing up.
       print('This distance is:', my_distance.get_distance())   

       # try 10 times and display the distance of the insect can fly
       print('I am going to test the distance ten times:')
       for count in range(10):
           my_distance.toss()
           
           # Display the side of the coin that is facing up.
           print('This distance is:', my_distance.get_distance())


# Call the main function.

main()
