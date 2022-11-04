
from datetime import datetime

animals = {}


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

    def add_event(self,event_type,event_name, event_date=datetime.now().date()):
        if event_type == 1:
            self.hist['sickness'].append((event_name,event_date))
            self.cond = event_name
        elif event_type == 2:
            self.hist['operation'].append((event_name,event_date))
            self.cond = event_name
        elif event_type == 3:
            self.hist['vaccination'].append((event_name,event_date))
        elif event_type == 4:
            self.cond = "healthy"
        elif event_type == 5:
            self.cond = "Sold"
            Animal.sold += 1
        else:
            return "Incorrect code"

    def get_info(self):
        return self.hist, self.name, self.cond, self.bday, self.species

    def get_id(self):
        return self.id


while True:
    event_code = int(input('0:create, 1: sickness, 2:operation, 3: vaccination, 4: heal, 5: sell, 6: inquiry, 7: quit'))
    if event_code == 7:
        break
    elif event_code == 0:
        name = input("Név?")
        species = input("Faj?")
        bday = input("Bday?")
        animal = Animal(name,species,bday)
        animals[animal.get_id()] = animal
    elif event_code == 6:
        animal_id = int(input("id?"))
        print(animals[animal_id].get_info())






