# bank.py
# this program prompts the user to read in two money amounts (in cent), adds the two amounts, and prints the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# author: gerry callaghan

amount1 =int(input("Enter the first amount (in cent):"))
amount2 =int(input("Enter the second amount (in cent):"))
#print(amount1)
#print(amount2)
result = amount1 + amount2


# Define a function which formats the currency string to euro
def format_currency(amount):
    amount = amount /100
    return '€{:,.2f}'.format(amount)

# Format a number as a currency string using defined function
currency_string = format_currency(result)
print(currency_string)




