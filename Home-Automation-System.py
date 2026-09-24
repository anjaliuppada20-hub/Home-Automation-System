# Home Automation System

print("===== HOME AUTOMATION SYSTEM =====")

light = False
fan = False
ac = False

while True:

    print("\n1. Turn ON Light")
    print("2. Turn OFF Light")
    print("3. Turn ON Fan")
    print("4. Turn OFF Fan")
    print("5. Turn ON AC")
    print("6. Turn OFF AC")
    print("7. Show Status")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        light = True
        print("Light is ON")

    elif choice == "2":
        light = False
        print("Light is OFF")

    elif choice == "3":
        fan = True
        print("Fan is ON")

    elif choice == "4":
        fan = False
        print("Fan is OFF")

    elif choice == "5":
        ac = True
        print("AC is ON")

    elif choice == "6":
        ac = False
        print("AC is OFF")

    elif choice == "7":
        print("\n===== DEVICE STATUS =====")
        print("Light:", "ON" if light else "OFF")
        print("Fan:", "ON" if fan else "OFF")
        print("AC:", "ON" if ac else "OFF")

    elif choice == "8":
        print("System closed.")
        break

    else:
        print("Invalid choice!")# Home-Automation-System
