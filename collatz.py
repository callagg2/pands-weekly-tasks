# This program asks a user to input any positive integer.

# It then outputs the successive values of the collatz calculation.

numbers = []

number = int(input("Please enter a positive integer: "))



# Take the current value and, 
while number != 1:
    numbers.append(number)
    if (number % 2) == 0: 
        number = number // 2
    else:
        number = (number*3) + 1
# numbers.append(number)

numbers.append(number)

print(f"Your path to one is \t {numbers}")
