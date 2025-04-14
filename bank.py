# bank.py
# this program prompts the user to read in two money amounts (in cent), 
# adds the two amounts, and prints the answer in a human readable format 
# with a euro sign and decimal point between the euro and cent of the amount 

# author: gerry callaghan

# the initial part of this exercise was covered around the 15 minute mark of this video
# https://atlantictu-my.sharepoint.com/personal/andrew_beatty_atu_ie/_layouts/15/stream.aspx
# where you input a number as an interger

amount1 =int(input("Enter the first amount (in cent):"))
amount2 =int(input("Enter the second amount (in cent):"))
#print(amount1) # this is me testing that the correct number is read in and output
#print(amount2) # this is me testing that the correct number is read in and output
result = (amount1 + amount2)/100 # we divide the addition by 100, because our number was in cent

#print(f"{result}") # this gives me only one place of decimal

# The format(amount,'.2f') i got from stackoverflow, and the 2f converts the amount to a number with two decimals
# and then using a standard f string, i merely place a euro symbol in front
# https://stackoverflow.com/questions/58171983/need-help-understanding-the-format-2f-command-and-why-it-is-not-working-in-my


print(f"€{format(result,'.2f')}")

# print(f"€{format(result,'.3f')}") # just confirming that this gives me 3 places of decimal