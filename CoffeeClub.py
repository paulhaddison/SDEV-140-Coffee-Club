# Program name: CoffeeClub
# Author: Paul Addison
# Date: 9/30/2021
# Summary: Front-end menu for maintaining coffee inventory
# Variables:
#   choice: user choice from the menu

import add_coffee_record
import show_coffee_records
import search_coffee_records
import modify_coffee_records
import delete_coffee_record

def main():
    # Create a loop control variable
    choice = -1

    # Loop to show and run menu items
    while choice != 9:
        print()
        print("Select 1 to add coffee records,")
        print("       2 to show coffee records,")
        print("       3 to search coffee records,")
        print("       4 to modify coffee records,")
        print("       5 to delete coffee records,")
        print("    or 9 to quit the program.")

        choice = int(input("Enter your choice: "))
        print()

        if choice == 1:
            add_coffee_record.add()
        elif choice == 2:
            show_coffee_records.show()
        elif choice == 3:
            search_coffee_records.search()
        elif choice == 4:
            modify_coffee_records.modify()
        elif choice == 5:
            delete_coffee_record.delete()
        elif choice != 9:
            print("ERROR...please choose 1, 2, 3, 4, 5, or 9:")

main()






            






            

        
