import math

current_drink_list = []


def bar_menu():
    print("1. Vodka \n")
    print("2. Rum \n")
    print("3. Whiskey \n")
    print("4. Beer \n")
    print("5. Quit Menu \n")
    while True:
        try:
            selection=int(input("Enter Choice: "))
            if selection == 1:
                vodka()
                break
            elif selection == 2:
                rum()
                break
            elif selection == 3:
                whiskey()
                break
            elif selection == 4:
                beer()
                break
            elif selection == 5:
                break
            else:
                print("Invalid Choice. Enter 1-5")
                bar_menu()
        except ValueError:
            print("Use a number you Knuckle-Head")
    exit

def vodka():
    print("\nYou choose: Vodka\n")
    print("18.99 \n")
    current_drink_list.append((18.99))
    print(drinks())


def rum():
    print("\nYou choose: Rum\n")
    print("12.99 \n")
    current_drink_list.append((12.99))
    print(drinks())


def whiskey():
    print("\nYou choose: Whiskey\n")
    print("15.99 \n")
    current_drink_list.append((15.99))
    print(drinks())


def beer():
    print("\nYou choose: Beer\n")
    print( "8.99 \n")
    current_drink_list.append((8.99))
    print(drinks())


def drinks(): 
    another_drink = int(input("Do you Want Another Drink? 1 = Yes, 2 = No.:"))
    if another_drink == 1:
        another_drink = print(bar_menu())
    elif another_drink == 2:
        print(show_total())
    else:
        print("Invaild choice you probably did this before!")


def show_total():
    Total_of_all = sum(current_drink_list)
    return Total_of_all

bar_menu()