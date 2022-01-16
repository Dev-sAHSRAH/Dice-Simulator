#importing module for random number generation
import random

#range of the values of a dice (1 to 6)
min_num = 1
max_num = 6

#to loop the rolling through user input
roll_again = "yes"

#loop
while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("The Number is :")
    
    #generating and printing 1st random integer from 1 to 6
    print(random.randint(min_num, max_num))
    
    #generating and printing 2nd random integer from 1 to 6
    #print(random.randint(min_num, max_num))
    
    #asking user to roll the dice again. Any input other than yes or y will terminate the loop
    roll_again = input('''"Roll the Dice Again?" 

(Please enter your choice as "yes" or "y" to continue OR
  any other character to stop.) \n''' ) 
    if roll_again!='y' or roll_again!="yes":
        print("Thank you for using Dice Simulator!")