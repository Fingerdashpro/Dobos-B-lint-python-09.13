# Create a simple IF function that compares nativeVLAN and dataVLAN values and prints result.
nativeVLAN = int(input("give the value of nativeVlan: "))
dataVLAN = int(input("now give the value of dataVLAN"))

if nativeVLAN == dataVLAN:
    print("Same VLAN")
else:
    print("Different VLAN")