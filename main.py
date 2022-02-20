import os
path = os.getcwd()
file_name = 'text.txt'
full_path = os.path.join(path, file_name)
cook_book = {}
list = []
chislo = 0
chislo_recipes = 0
slovar = {}
class Slovar:
    def __init__(self, ingridient_name, quantity, measure):
        self.ingridient_name = ingridient_name
        self.quantity = quantity
        self.measure = measure
        self.slovar = {}
    def add_slovar(self):
        self.slovar['ingridient_name'] = self.ingridient_name
        self.slovar['quantity'] = self.quantity
        self.slovar['measure'] = self.measure.rstrip()
        list.append(self.slovar)

with open(full_path, 'r', encoding='utf-8') as file:
    for line in file:
        if line == '\n':
            chislo += 1
with open(full_path, 'r', encoding='utf-8') as file:
    def read_recipe():
        dish_name = file.readline()
        number = int(file.readline())
        i = 0
        while i < number:
            count = 0
            ingridient_name = ''
            quantity = ''
            measure = ''
            i += 1
            string = file.readline()
            for symbol in string:
                if symbol != '|':
                    if symbol != ' ':
                        if count == 0:
                            ingridient_name += symbol
                        if count == 1:
                            quantity += symbol
                        if count == 2:
                            measure += symbol
                else:
                    count += 1
            slovar = Slovar(ingridient_name, quantity, measure)
            slovar.add_slovar()
        cook_book[dish_name.rstrip()] = list
    read_recipe()
    list = []
    while (chislo_recipes < chislo):
        chislo_recipes += 1
        if file.readline() == '\n':
            read_recipe()
            list = []
print(cook_book)
def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        for ingridient in cook_book[dish]:
            slovar_2 = {}
            slovar_2['quantity'] = 0
            if ingridient['ingridient_name'] in slovar:
                slovar[ingridient['ingridient_name']]['quantity'] += int(ingridient['quantity']) * person_count
            else:
                slovar_2['measure'] = ingridient['measure']
                slovar_2['quantity'] = int(ingridient['quantity']) * person_count
                slovar[ingridient['ingridient_name']] = slovar_2
    print(slovar)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)