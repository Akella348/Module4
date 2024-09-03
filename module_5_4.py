class House:
    houses_history = []

    def __new__(cls, *name, **number_of_floors):
       if cls.houses_history is None:
           cls.houses_history = super().__new__(cls)
       cls.houses_history.append(name[0])
       #return cls.houses_history

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    # def go_to(self, new_floor):
    #     if new_floor > self.number_of_floors:
    #         print('Такого этажа нет')
    #     else:
    #         for i in range(1, new_floor+1):
    #             print(i)


    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name},кол-во этажей: {self.number_of_floors}')
    def __eq__(self, other):
        if isinstance(other, int) == True:
            return self.number_of_floors == other
        elif isinstance(other, House) == True:
            return self.number_of_floors == other.number_of_floors
        else:
            print("Неверный тип данных")

    def __lt__(self, other):
        if isinstance(other, int) == True:
            return self.number_of_floors < other
        elif isinstance(other, House) == True:
            return self.number_of_floors < other.number_of_floors
        else:
            print("Неверный тип данных")
    def __le__(self, other):
        if isinstance(other, int) == True:
            return self.number_of_floors <= other
        elif isinstance(other, House) == True:
            return self.number_of_floors <= other.number_of_floors
        else:
            print("Неверный тип данных")
    def __gt__(self, other):
        if isinstance(other, int) == True:
            return self.number_of_floors > other
        elif isinstance(other, House) == True:
            return self.number_of_floors > other.number_of_floors
        else:
            print("Неверный тип данных")
    def __ge__(self, other):
        if isinstance(other, int) == True:
            return self.number_of_floors >= other
        elif isinstance(other, House) == True:
            return self.number_of_floors >= other.number_of_floors
        else:
            print("Неверный тип данных")
    def __ne__(self, other):
        if isinstance(other, int) == True:
            return self.number_of_floors != other
        elif isinstance(other, House) == True:
            return self.number_of_floors != other.number_of_floors
        else:
            print("Неверный тип данных")
    def __add__(self, value):
        if isinstance(value, int) == True:
            self.number_of_floors += value
            return self
        elif isinstance(value, House) == True:
            self.number_of_floors += value.number_of_floors
            return self
        else:
            print("Неверный тип данных")
    def __radd__(self, value):
        if isinstance(value, int) == True:
            self.number_of_floors += value
            return self
        elif isinstance(value, House) == True:
            self.number_of_floors += value.number_of_floors
            return self
        else:
            print("Неверный тип данных")
    def __iadd__(self, value):
        if isinstance(value, int) == True:
            self.number_of_floors += value
            return self
        elif isinstance(value, House) == True:
            self.number_of_floors += value.number_of_floors
            return self
        else:
            print("Неверный тип данных")
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
