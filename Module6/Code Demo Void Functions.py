# This program illustrates use of user defined void functions
# A health club offers three categories of rates
# User selects membership type and months and charges are displayed

CHILD = 20.00       # monthly rate for child (0..17)
ADULT = 40.00       # monthly rate for adult (18..64)
SENIOR = 30.00      # montly rate for senior (65+)

def main():
    # show the menu
    show_menu()

    # process user choices 
    choice =  input('Enter choice from menu: ')
    while choice != 'Q':
        # call function with correct rate 
        if choice == 'C':
            show_fees(CHILD)        
        elif choice == 'A':
            show_fees(ADULT)
        elif choice == 'S':
            show_fees(SENIOR)
        else:
            print ('Please enter valid choice')
            print()      
        choice =  input('Enter choice from menu: ')    
    
# display membership menu with prices
def show_menu():
    print ()
    print ('Health Club Membership Menu')
    print (f'Select A for Adult membership with monthly rate ${ADULT:.2f}')
    print (f'Select C for Child membership with monthly rate ${CHILD:.2f}')
    print (f'Select S for Senior membership with monthly rate ${SENIOR:.2f}')
    print ('Select Q to quit')
    print ()

# compute and display rates based on member rate and months
def show_fees(member_rate):
    months = int(input('Enter number of months (1..24): '))
    while months < 1 or months > 24:
        print ('Enter months in range 1..24')
        months = int(input('Enter number of months (1..24): '))
               
    # compute charges based on months
    charges = member_rate * months
    print (f'Total Charges: ${charges:.2f}')
    print ()


main()
    
    
