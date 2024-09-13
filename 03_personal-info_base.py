"""
Write code to get output below:

What is your first name? First
What is your last name? Last
What is your location? Texas
What is your age? 54
Hi First Last! Your location is Texas and you are 54 years old.
>>>
"""
first = input("What is your first name?") 
last = input("What is your last name?") 
locat = input("What is your location?") 
age =int(input("What is your age?"))

print(f"Hi {first} {last}! Your location is {locat} and you are {age} years old. ")