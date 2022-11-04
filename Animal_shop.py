from datetime import datetime
from animal_class import Animal
import time
from Actions_enum import Actions

animals_dict = {}

#Print a menu with the avaliable options
#Dynamic numbers, which come from the Actions class in Actions_enum.py file
def print_menu():
    print(10* '-' + 'MENU' + 10*'-')
    print(f'Press {Actions.create.value} to create')
    print(f'Press {Actions.sick.value} to log sickness')
    print(f'Press {Actions.operation.value} to log operation')
    print(f'Press {Actions.heal.value} to log healing')
    print(f'Press {Actions.vaccine.value} to log vaccination')
    print(f'Press {Actions.inquire.value} to inquire')
    print(f'Press {Actions.sell.value} to sell')
    print(f'Press {Actions.quit.value} to quit')
    print(24*'-')

while True:
    print_menu()
    event_code = int(input('Please enter the command: '))

    #Quiting the app
    if event_code == Actions.quit.value:
        break
    
    #Creating a new object instance
    elif event_code == Actions.create.value:
        #Getting neccesary input data for object
        name = input("Enter a name: ")
        species = input("Enter the species: ")
        bday = input("Please enter the birtday of the animal (YYYY-MM-DD): ")

        #Creating a temp object with inputs, then assigning that to a new dictionary item in animals_dict with the key of the animal's ID
        animal_temp = Animal(name,species,bday)
        animals_dict[animal_temp.get_id()] = animal_temp

        #Giving user feedback, with the generated ID, then waiting 2 seconds to get back to menu
        print(f'Created an animal with the ID: {animal_temp.get_id()}')
        time.sleep(2)

    #Getting the data of the animal
    elif event_code == Actions.inquire.value:
        animal_id = int(input("Please enter the ID of the animal: "))
        print(animals_dict[animal_id].get_info())


