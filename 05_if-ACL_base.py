'''
The standard ACL numbers are between 1 and 99 (inclusive)
The extended ACL numbers are between 100 199 (inclusive)
Other ACL numbers are nor standard nor extended.
Input an ACL number and categorize it!
'''
szam = int(input("give me a number between 1 and 199: "))

if szam <100:
    print("Your number is standard ACL")
elif szam >199:
    print("Your number isn't standard nor extended ACL")
else:
    print("Your number is extended ACL")