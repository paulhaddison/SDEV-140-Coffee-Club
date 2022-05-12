# This program displays the records in the
# coffee.txt file.
import os

def show():
    try:
        # Open the coffee.txt file.
        coffee_file = open('coffee.txt', 'r')

    except IOError:
        print("File does not exist. Please select add first.")
        os._exit(0)

    # Read the first record's description field.
    descr = coffee_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(coffee_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # Display the record.
        print('Description:', descr)
        print('Quantity:', qty)

        # Read the next description.
        descr = coffee_file.readline()

    # Close the file.
    coffee_file.close()




