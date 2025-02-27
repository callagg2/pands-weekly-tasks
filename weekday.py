# a program that outputs whether or not today is a weekday

# author: gerry callaghan

#weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

'''
day = str(input("Enter in what day it is to confirm if it is a weekday: "))
if day in weekdays:
    print(f"Yes, unfortunately today is a weekday.")
else:
    print(f"It is the weekend, yay!")
'''

'''
import datetime
#day = datetime.datetime.now()
#print(type(day))
#print(day.strftime("%A"))
'''
# using built in functions according to https://www.w3schools.com/python/python_datetime.asp
import datetime
today = datetime.datetime.now()
day = int((today.strftime("%w")))
#print(weekdays[day.strftime("%w")])
#print(type(day))

if day <=5:
    print(f"Yes, unfortunately today is a weekday.")
else:
    print(f"It is the weekend, yay!")