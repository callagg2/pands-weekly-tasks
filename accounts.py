# This program reads in a 10 character account number 
# and outputs the account number with only the last 4 digits showing 
# (and the first 6 digits replaced with Xs).

# Author: Gerry Callaghan

account_number = input("Please enter an 10 digit account number:")

# Andrew talks about this around 17 minutes in this lecture https://atlantictu-my.sharepoint.com/personal/andrew_beatty_atu_ie/_layouts/15/stream.aspx
# I did this in the third lab exercise to normalise a number, put everything into lowercase and remove spaces
normalised_account_number = account_number.strip().lower()

# Modify the program to deal with account numbers of any length 
# information on string length can be found here https://www.w3schools.com/python/python_strings.asp
valid_length = len(normalised_account_number)

# I'm going to assume that if the number is greater than 10 characters I can reject
# using the if else example from W3schools
if valid_length == 10: 
    print(f"This is a valid {valid_length} digit number.")
    # using the splicing example in https://www.w3schools.com/python/python_strings_slicing.asp
    # we start at 6 and go to the end (we could also start at the end and using negative values of -4)
    print(f"xxxxxx{normalised_account_number[6:]}")
else: 
    print(f"This is not a valid 10 digit number, it has {valid_length} digits.")






