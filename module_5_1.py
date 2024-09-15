class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.namber_of_floors = number_of_floors

    def go_to(self, new_floor):

        if new_floor > self.namber_of_floors or new_floor < 1:
            print('Такого этажа не существует')

        elif new_floor < self.namber_of_floors or new_floor > 1:

            for i in range(1, new_floor):
                print(i)


h1 = House('ЖК Эльбрус', 30)
h2 = House('Общежитие', 5)
h1.go_to(5)
h2.go_to(7)
