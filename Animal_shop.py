from datetime import datetime
from animal_class import Animal
import time
from Actions_enum import Actions

animals_dict = {}

#Print a menu with the avaliable options
#Dynamic numbers, which come from the Actions class in Actions_enum.py file
def print_menu():
    print(10* '-' + 'MENU' + 10*'-')
    print(f'Press {Actions.create.value} to create') #Done
    print(f'Press {Actions.sick.value} to log sickness') #Done
    print(f'Press {Actions.operation.value} to log operation') #Done
    print(f'Press {Actions.heal.value} to log healing') #Done
    print(f'Press {Actions.vaccine.value} to log vaccination') #Done
    print(f'Press {Actions.inquire.value} to get animal data') #Done
    print(f'Press {Actions.history.value} to get the history of an animal') #Done
    print(f'Press {Actions.list.value} to list animal names and IDs') #Done
    print(f'Press {Actions.sell.value} to sell')
    print(f'Press {Actions.quit.value} to quit') #Done
    print(24*'-')

#Require users to press enter before returning to main menu
def enter_to_continue():
    continue_to_next = input('Press enter to continue to main menu!')
    if continue_to_next is True:
            pass
    
while True:
    print_menu()
    event_code = int(input('Please enter the command: '))

    #Quiting the app
    if event_code == Actions.quit.value:
        break

    #List all animals and their ID's
    elif event_code == Actions.list.value:
        print('You have the following animals in your database:')
        for k,v in animals_dict.items():
            print(f'The animal called {v.name}, who is a(n) {v.species}, has an ID of {k}')
        enter_to_continue()

    #Sell an animal
    elif event_code == Actions.sell.value:
        animal_id = int(input('Please enter the ID of the animal: '))
        are_you_sure = input(f'Are you sure you want to remove {animals_dict[animal_id].name} from the database (y/n): ')
        if are_you_sure == 'y':
            print(f'Removed {animals_dict[animal_id].name} from the database.')
            animals_dict.pop(animal_id)
            enter_to_continue()
        else:
            pass

    #Add healing to animal
    elif event_code ==Actions.heal.value:
        animal_id = int(input("Please enter the ID of the animal: "))
        animals_dict[animal_id].heal()
        print(f'{animals_dict[animal_id].name} has been healed!')
        enter_to_continue()
        
    #Get history of the animal
    elif event_code == Actions.history.value:
        animal_id = int(input("Please enter the ID of the animal: "))
        history_type = int(input(f'Please enter the type of history: {Actions.sick.value} for sicknesses, {Actions.operation.value} for operations and {Actions.vaccine.value} for vaccinations: '))

        print(animals_dict[animal_id].get_history(history_type))
        enter_to_continue()

    #Add a sickness to an animal
    elif event_code == Actions.sick.value:
        id_to_modify = int(input('Please enter an animal ID to register sickness to: '))
        sickness_name = input('Please enter the name of the sickness: ')
        is_current = input('Is this a current sickness? y/n: ')

        if is_current == 'y':
            animals_dict[id_to_modify].add_event(Actions.sick.value, sickness_name)
            animals_dict[id_to_modify].cond = 'Sick'
        elif is_current == 'n':
            date_of_event = input('Please enter when the event took place (YYYY-MM-DD): ')
            animals_dict[id_to_modify].add_event(Actions.sick.value, sickness_name, date_of_event)
        else:
            print('Please enter a valid answer (y/n)')
        
        print(f'Added sickness ({sickness_name}) to animal called {animals_dict[id_to_modify].name}')

        enter_to_continue()
    
    #Add operation to an animal
    elif event_code == Actions.operation.value:
        id_to_modify = int(input('Please enter an animal ID to register operation to: '))
        operation_name = input('Please enter the name of the operation: ')
        date_of_event = input('Please enter when the event took place (YYYY-MM-DD): ')

        #Add operation to object
        animals_dict[id_to_modify].add_event(Actions.operation.value, operation_name, date_of_event)
        print(f'Added operation ({operation_name}) to animal called {animals_dict[id_to_modify].name}')
        enter_to_continue()

    #Add vaccination to an animal
    elif event_code == Actions.vaccine.value:
        id_to_modify = int(input('Please enter an animal ID to register vaccination to: '))
        vaccine_name = input('Please enter the name of the vaccine: ')
        date_of_event = input('Please enter when the event took place (YYYY-MM-DD): ')

        #Add vaccination to object
        animals_dict[id_to_modify].add_event(Actions.vaccine.value, vaccine_name, date_of_event)
        print(f'Added vaccine ({vaccine_name}) to animal called {animals_dict[id_to_modify].name}')
        enter_to_continue()

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

        enter_to_continue()

    #Getting the data of the animal
    elif event_code == Actions.inquire.value:
        animal_id = int(input("Please enter the ID of the animal: "))
        tuple1 = animals_dict[animal_id].get_info()
        for i in tuple1:
            print(i)
        enter_to_continue()
