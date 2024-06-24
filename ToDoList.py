print("Hello ToDo List Program")

print("Select Your Day")
print("1-Monday")
print("2-Tuesday")
print("3-Wednesday")
print("4-Thursday")
print("5-Friday")
print("6-Saturday")
print("7-Sunday")
x = input("1/2/3/4/5/6/7: ")

if x == "1":
    day = "Monday"
elif x == "2":
    day = "Tuesday"
elif x == "3":
    day = "Wednesday"
elif x == "4":
    day = "Thursday"
elif x == "5":
    day = "Friday"
elif x == "6":
    day = "Saturday"
elif x == "7":
    day = "Sunday"
else:
    print("Invalid input. Please restart the program and select a valid day.")
    exit()

print(f"Write Your Plans for {day}")
plan1 = input("Write Your First Plan: ")
plan2 = input("Write Your Second Plan: ")
plan3 = input("Write Your Third Plan: ")
plan4 = input("Write Your Fourth Plan: ")
plan5 = input("Write Your Fifth Plan: ")
plan6 = input("Write Your Sixth Plan: ")

print("Write Your Clocks")
time1 = input("First Clock: ")
time2 = input("Second Clock: ")
time3 = input("Third Clock: ")
time4 = input("Fourth Clock: ")
time5 = input("Fifth Clock: ")
time6 = input("Sixth Clock: ")

print(f"\nYour plans for {day}:")
print(f"{time1} - {plan1}")
print(f"{time2} - {plan2}")
print(f"{time3} - {plan3}")
print(f"{time4} - {plan4}")
print(f"{time5} - {plan5}")
print(f"{time6} - {plan6}")
