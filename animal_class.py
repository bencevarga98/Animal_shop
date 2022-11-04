from datetime import datetime
from Actions_enum import Actions

class Animal:
    sold = 0
    total = 0
    id_num = 1

    def __init__(self,name,species,bday):
        self.name = name
        self.id = Animal.id_num
        Animal.id_num += 1
        self.hist = {'sickness':[],'operation':[],'vaccination':[]}
        self.species = species
        self.bday = bday
        self.cond = "healthy"
        Animal.total += 1

'''
Menu options:
class Actions(Enum):
    create = 1
    sick = 2
    operation = 3
    heal = 4
    vaccine = 5
    inquire = 6
    sell = 7
    quit = 8
'''


def add_event(self,event_type,event_name, event_date=datetime.now().date()):
    if event_type == Actions.sick.value:
        self.hist['sickness'].append((event_name,event_date))
        self.cond = event_name
    elif event_type == Actions.operation.value:
        self.hist['operation'].append((event_name,event_date))
        self.cond = event_name
    elif event_type == Actions.vaccine.value:
        self.hist['vaccination'].append((event_name,event_date))
    elif event_type == Actions.heal.value:
        self.cond = "healthy"
    elif event_type == Actions.sell.value:
        self.cond = "Sold"
        Animal.sold += 1
    else:
        return "Incorrect code"

def get_info(self):
    return self.hist, self.name, self.cond, self.bday, self.species

def get_id(self):
    return self.id
