import CoinClass as c
#import the CoinClass.py file - import the name of the file 
#not the class itself 
#everything in the CoinClass file are avaialble here 


# The main function.
def main():
       # Create an object from the Coin class.
       my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'

       # Display the side of the coin that is facing up.
       print('This side is up:', my_coin.get_sideup())    # notice you do not have to supply the argument/parameter

       # Toss the coin.
       print('I am going to toss the coin ten times:')
       for count in range(10):
           my_coin.toss()
           
           #IF WE ADD ONE MORE LINE 
           #THE RESULT WILL BE ALL HEADS 
           #my_coin.sideup = 'Heads' 

           #this will not work - When we add __ before the attributes 
           #and the hack will not work because the change 
           #will only be made from the coinClass file 


           # Display the side of the coin that is facing up.
           print('This side is up:', my_coin.get_sideup())

           


       

# Call the main function.

main()
