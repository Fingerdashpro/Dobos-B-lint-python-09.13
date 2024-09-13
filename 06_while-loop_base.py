'''
Write Python program :
    get an input for a number to count to
    if input is "q" or "quit", the program exits
    else write numbers from 1 to the number in one line, separated by space and goes back to the input
'''
while True:
    szamvq = input("Enter a number to count to (or 'q' to exit): ")

    if szamvq in ('q'):
        print("Exiting the program.")
        break

    if szamvq:
        counto = int(szamvq)
        if counto > 0:
            print(" ".join(str(i) for i in range(1, counto + 1)))
        else:
            print("Please enter a positive number.")
    else:
        print("Invalid input. Please enter a valid number or 'q' to exit.")