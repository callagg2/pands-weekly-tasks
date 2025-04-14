# This program asks a user to input any positive integer.

# It then outputs the successive values of the collatz calculation.

# author: gerry callaghan

# we first set establish a blank array
numbers = []

# we now prompt the user to input an integer, and convert the input to an integer for coding purposes
number = int(input("Please enter a positive integer: "))

# here are some python operators that we will use  https://www.w3schools.com/python/python_operators.asp
# % Modulus (that is divide a number by another and find its remainder)
# // floor division (that is divides one number by another and rounds to the nearest lower number
# * just multiplication)

# using the while loop covered in this week's  class https://atlantictu-my.sharepoint.com/personal/andrew_beatty_atu_ie/_layouts/15/stream.aspx
# and the fifth exercise in the lab 

# Take the current value that was input 
while number != 1: # if the number input by the user is not equal to one
    numbers.append(number) # we append it to our array called numbers
    if (number % 2) == 0: # if we divide that number by any multiple of 2 equals 0
        number = number // 2  # we divide that number by two and round it to the nearest whole (lower) number
    else:
        number = (number*3) + 1 # otherwise we multiply the number by 3 and add 1

# this then appends the last instance of number (which must be 1 if we exit the while loop) to our array called numbers
numbers.append(number)

# now we print out the variable numbers which is our array
print(f"Your path to one is \t {numbers}")
