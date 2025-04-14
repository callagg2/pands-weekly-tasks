# a program that outputs whether or not today is a weekday

# author: gerry callaghan

'''
# this would work if user input were allowed, but we're told explicitly that it is not :-(

#weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

day = str(input("Enter in what day it is to confirm if it is a weekday: "))
if day in weekdays:
    print(f"Yes, unfortunately today is a weekday.")
else:
    print(f"It is the weekend, yay!")
'''


# using built in functions according to https://www.w3schools.com/python/python_datetime.asp
import datetime # we must import this function

today = datetime.datetime.now() # we initialise the value of our variable called "today" equal 
# to what the function datatime says the date at the time it is called

# print(type(today)) #this function tells me that the variable today is <class 'datetime.datetime'>
# according to w3schools  it looks like this 2025-04-14 21:21:46.122694
# so i can't use that in an if statement as i want

# so let's make an integer variable day that is the number of the week according to the datetime that the variable today possesses
# according to w3schools on datetime, using the strftime() method, pasing the string "%w" returns Weekday as a number 0-6, 0 is Sunday
day = int((today.strftime("%w")))
# print(type(day)) # now we know that day is an integer

#print(weekdays[day.strftime("%w")])


if day <=5: # we know from aboe that 0 is Sunday, so Monday must be 1 and Friday 5, so a weekend must when day is any value between 1 and 5 incl
    print(f"Yes, unfortunately today is a weekday.")
else: # if day has a value other than that, it must be a weekend
    print(f"It is the weekend, yay!")

