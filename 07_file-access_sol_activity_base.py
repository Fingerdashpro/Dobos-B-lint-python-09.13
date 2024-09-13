with open("devices.txt", "a") as file:
    while True:
        newItem = input("Enter device name or type exit to end: ")
        if newItem.lower() == "exit":
            print("All done!")
            break
        file.write(newItem + "\n")

