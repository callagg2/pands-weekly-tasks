# this program divides one number by another
# author: gerry callaghan

x=int(input("Enter first number:"))
y=int(input("Enter the number you want to divide by:"))

answer = x//y
remainder = x%y

print(f"{x} divided by {y} is {answer} with remainder {remainder}")