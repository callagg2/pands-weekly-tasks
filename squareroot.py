# We create our own sqrt function based on Newton's method

# author: gerry callaghan

# using the formula from here https://www.youtube.com/watch?v=FpOEx6zFf1o

number_to_be_rooted = float(input("Please enter a positive number: "))

def sqrt(number_to_be_rooted):
    improved_guess = 0.5*number_to_be_rooted
    change_in_improved_guess = 1
    
    while change_in_improved_guess != 0:
        last_guess = improved_guess
        improved_guess = 0.5*(improved_guess + number_to_be_rooted/improved_guess)
        change_in_improved_guess = improved_guess - last_guess
    return round(improved_guess,1)

print(f"The square root of {number_to_be_rooted} is approx. {sqrt(number_to_be_rooted)}")

