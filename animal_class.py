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
        self.cond = "Healthy"
        Animal.total += 1

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
        return f'The name of the animal is {self.name} \n', f'The species of the animal is {self.species} \n', f'The condition of the animal is {self.cond} \n', f'The bday of the animal is {self.bday} \n'

    def get_id(self):
        return self.id

    def get_history(self, history_type):
        if history_type == Actions.sick.value:
            #return sicknesses
            return(self.hist['sickness'])

        elif history_type == Actions.operation.value:
            #return operations
            return(self.hist['operation'])

        elif history_type == Actions.vaccine.value:
            #return vaccination history
            return(self.hist['vaccination'])
    
    def heal(self):
        self.cond = 'Healthy'
