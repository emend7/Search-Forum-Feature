# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sqlite3

import objecttier

# have a few options on how many items you want to search for

# usecase 1: want to search by product id tag
# usecase 2: want to search by product name
# usecase 3: want to search by industry
# usecase 4: want to search by problem

# Press the green button in the gutter to run the script.
print("** Welcome to the Search Forum Database Application")
print('** Welcome to the Chicago Lobbyist Database Application **\n')
print()

choice = input("Please enter a command (1-5, x to exit): ")

while choice != "x":
    if choice == "1":
        # usecase 1: want to search by product id tag
        pass
    elif choice == "2":
        # usecase 2: want to search by product name
        pass
    elif choice == "3":
        # usecase 3: want to search by industry
        pass
    elif choice == "4":
        # usecase 4: want to search by problem
        pass
    else:
        print("**Error, unknown command, try again...\n")

    choice = input("Please enter a command (1-4, x to exit): ")

#
# done
#
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
