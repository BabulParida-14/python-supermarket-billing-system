# write a program to create a billing system at supermarket.

while True:
    name = input("Enter customer's name :")
    total = 0

    while True:
        print("Enter the amount and quantity ")
        amount = int(input("Enter amount :"))
        quantity = int(input("Enter Quantity : "))
        total += amount * quantity
        repeat = input("Do you want more iteam? (yes/no) : ")
        if repeat == "no" or repeat == "No":
            break
    print("_"*40)
    print("Name : ",name)
    print("Amount to be paid : ",total)
    print("-"*40)
    print("Happy shopping")
    repeat1 = input("Do you want to go to next customr? (yes/no):")
    if repeat1 =="no" or repeat1 == "No":
        break
