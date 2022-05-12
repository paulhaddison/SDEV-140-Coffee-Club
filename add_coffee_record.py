# This program adds coffee inventory records to
# the coffee.txt file.

def add():
    # Create a variable to control the loop.
    another = 'y'

    # Open the coffee.txt file in append mode.
    coffee_file = open('coffee.txt', 'a')

    # Add records to the file.
    while another == 'y' or another == 'Y':
        # Get the coffee record data.
        print('Enter the following coffee data:')
        descr = input('Description: ')
        qty = input('Quantity (in pounds): ')
        while not qty.isnumeric():
            print("ERROR...you must enter a numeric amount.")
            qty = input('Quantity (in pounds): ')
        else:
            qty = int(qty)
            

        # Append the data to the file.
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')

        # Determine whether the user wants to add
        # another record to the file.
        print('Do you want to add another record?')
        another = input('Y = yes, anything else = no: ')

    # Close the file.
    coffee_file.close()
    print('Data appended to coffee.txt.')


        
