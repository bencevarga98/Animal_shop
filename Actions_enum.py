from enum import Enum

class Actions(Enum):
    create = 1
    sick = 2
    operation = 3
    heal = 4
    vaccine = 5
    inquire = 6
    history = 7
    list = 8
    sell = 9
    quit = 10

# Print a menu with the avaliable options
# Dynamic numbers, which come from the Actions class in Actions_enum.py file
def print_menu():
    print(10 * '-' + 'MENU' + 10 * '-')
    print(f'Press {Actions.create.value} to create')  
    print(f'Press {Actions.sick.value} to log sickness')  
    print(f'Press {Actions.operation.value} to log operation')  
    print(f'Press {Actions.heal.value} to log healing')  
    print(f'Press {Actions.vaccine.value} to log vaccination')  
    print(f'Press {Actions.inquire.value} to get animal data')  
    print(f'Press {Actions.history.value} to get the history of an animal')  
    print(f'Press {Actions.list.value} to list animal names and IDs')  
    print(f'Press {Actions.sell.value} to sell') 
    print(f'Press {Actions.quit.value} to quit')  
    print(24 * '-')

# Require users to press enter before returning to main menu
def enter_to_continue():
    continue_to_next = input('Press enter to continue to main menu!')
    if continue_to_next is True:
        pass