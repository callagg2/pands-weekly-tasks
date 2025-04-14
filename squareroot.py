# We create our own sqrt function based on Newton's method
# I'm going to leave the filename as squareroot instead of sqrt in case a filename of sqrt causes issues with inbuilt functions

# author: gerry callaghan

# using the formula from here https://www.youtube.com/watch?v=FpOEx6zFf1o

# we promt the user to enter a number, and make it a floating number (i say a float because in the assignment the input of 14.5 is used )
number_to_be_rooted = float(input("Please enter a positive number: "))

def sqrt(number_to_be_rooted):
    improved_guess = 0.5*number_to_be_rooted # this is just a rough approx
    change_in_improved_guess = 1 # this is my initialisation of my variable for the upcoming while loop
    
    while change_in_improved_guess != 0: # if it is zero, then stop trying to improve on my calculation it is making no improvement
        last_guess = improved_guess # so set my last guess equal to the improved guess before improving my guess yet further
        improved_guess = 0.5*(improved_guess + number_to_be_rooted/improved_guess) # according to the maths in the youtube channel
        change_in_improved_guess = improved_guess - last_guess # so now i subtract my previous guess and my new improved guess
        # to see how little of a difference there is, because if it is 0, i want to stop my while loop
    return round(improved_guess,1) # output the final improved guess

# so the following print function, take the number input by the user, and passes it into my newly created function "sqrt"
# which is designed to output a number
print(f"The square root of {number_to_be_rooted} is approx. {sqrt(number_to_be_rooted)}")

