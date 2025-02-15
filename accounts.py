# This program reads in a 10 character account number 
# and outputs the account number with only the last 4 digits showing 
# (and the first 6 digits replaced with Xs).

# Author: Gerry Callaghan

account_number = input("Please enter an 10 digit account number:")
normalised_account_number = account_number.strip().lower()

# Modify the program to deal with account numbers of any length 
# I'm going to assume that if the number is greater than 10 characters I can reject

valid_length = len(normalised_account_number)

# using the if else example from W3schools
if valid_length == 10: 
    print(f"This is a valid {valid_length} digit number.")
    # using the splicing example in w3schools
    print(f"xxxxxx{normalised_account_number[6:]}")
else: 
    print(f"This is not a valid 10 digit number, it has {valid_length} digits.")






