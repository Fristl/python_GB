"""В данном коде реализован проект СКЛАД"""

import copy


class Warehouse:

    equip_dct = {}
    sum_in_wh = {}

    def __init__(self, name):
        self.name_warehouse = name
        self.equip_dct = {}
        self.sum_in_warehouse = {}

    def get_equip(self, obj, count: int):
        while True:
            try:
                count = int(count)
                break
            except:
                count = input('Введите заново число поставленной техники: ')

        if obj.type_eq in self.equip_dct:
            spam = copy.deepcopy(obj.__dict__)
            spam.update(count=count)
            self.equip_dct[obj.type_eq].append(spam)
        else:
            self.equip_dct[obj.type_eq] = []
            spam = (copy.deepcopy(obj.__dict__))
            spam.update(count=count)
            self.equip_dct[obj.type_eq].append(spam)
        Warehouse.total_sum(self)

    def give_equip(self, type, count: int):
        while True:
            try:
                count = int(count)
                break
            except:
                count = input('Введите заново число забираемой техники: ')

        if type in self.sum_in_warehouse.keys():
            if count <= self.sum_in_warehouse[type]:
                self.sum_in_warehouse[type] -= count
            else:
                var = count - self.sum_in_warehouse[type]
                self.sum_in_warehouse[type] = 0
                print(f'Не хватило {var} {type}!')
        else:
            print(f'Предмета типа {type} нет на складе {self.name_warehouse}!')

    def total_sum(self):
        for i in self.equip_dct:
            self.sum_in_warehouse[i] = 0
            for item in self.equip_dct[i]:
                self.sum_in_warehouse[i] += item['count']
        return self.sum_in_warehouse

    # def total_in_gen_wh(self):
    #     for key, volume in self.sum_in_warehouse.items():
    #         if key not in Warehouse.sum_in_wh.keys():
    #             Warehouse.sum_in_wh[key] = volume
    #         else:
    #             Warehouse.sum_in_wh[key] += volume
    #     return Warehouse.sum_in_wh


class OfficeEquipment:

    def __init__(self, name, brand, **kwargs):
        self.type_eq = type(self).__name__.lower()
        self.name = name
        self.brand = brand
        self.__dict__.update(kwargs)


class Printer(OfficeEquipment):
    pass


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass


printer_1 = Printer('3220', 'hp', speed=25)
printer_2 = Printer('2567', 'xerox', speed_of=20)
scanner_1 = Scanner('45454', 'dell', sc=7)
xerox_1 = Xerox('34hg', 'xerox', instal='table')


W1 = Warehouse('warehouse_1')
W1.get_equip(printer_1, 5)
W1.get_equip(printer_2, 10)
W1.get_equip(scanner_1, 7)
W1.get_equip(scanner_1, 7)
print(W1.sum_in_warehouse)


W2 = Warehouse('warehouse_2')
W2.get_equip(printer_1, 5)
W2.get_equip(printer_1, 5)
W2.get_equip(printer_2, 10)
W2.get_equip(scanner_1, 7)
W2.get_equip(xerox_1, 11)
print(W2.sum_in_warehouse)

W1.give_equip('xerox', 5)
W2.give_equip('printer', 25)
print(W1.sum_in_warehouse)
print(W2.sum_in_warehouse)
