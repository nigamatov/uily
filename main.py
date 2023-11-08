class Passport:

    def init(self, first_name, last_name,country, date_ot_birth, num_of_passport):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.date_ot_birth = date_ot_birth
        self.num_of_passport = num_of_passport

    def printInfo(self):
        print(f'''
Full name: {self.first_name} {self.last_name}
Date of Birth: {self.date_ot_birth}
Country: {self.country}
Passport: {self.num_of_passport}
''')

p = Passport('Iven','Ivenov','Russia','14.05.2005','8221 457896')
p.printInfo()

class Equipment:

    def init(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def action(self):
        return 'не определено'

    def str(self):
        return f'{self.name}, {self.make}, {self.year}'

    def le(self, other):
        if not isinstance(other, Equipment):
            raise TypeError
        return self.year <= other.year

class Printer(Equipment):

    def init(self, series, name, make, year):
        super().init(name, make, year)
        self.series = series

    def action(self):
        return 'печатает'

    def str(self):
        return f'{self.series} {self.name}, {self.make}, {self.year}'

class Scaner(Equipment):

    def  init(self, name, make, year):
        super().init(name, make, year)

    def action(self):
        return 'сканирует в комп'

class Xerox(Equipment):

    def init(self, name, make, year):
        super().init(name, make, year)

    def action(self):
        return 'копирует и печатает на листочек'

def allItems(sklad):
    for item in sklad:
        print(item)

def get_items(sklad, ename):
    for item in sklad:
        if isinstance(item, ename):
            print(item)

sklad = []
e = Equipment('Noname', 'X', 2000)
sklad.append(e)
s = Printer('H451','dsfsdf', 'asdasd', 1545)
sklad.append(s)
x = Xerox('sdfsdf', 'sdfsdf', 5000)
sklad.append(x)
e = Equipment('Noname', 'X', 2000)
sklad.append(e)
s = Printer('TH84','dsfsdf', 'asdasd', 1545)
sklad.append(s)
x = Xerox('sdfsdf', 'sdfsdf', 5000)
sklad.append(x)
allItems(sklad)
qet_items(sklad, Equipment)

from random import randint
class Soldier:

    def init(self, name='Noname', health=100):
        self.name = name
        self.health = health

    def set_name(self, name):
        self.name = name

    def make_kick(self, enemy):
        enemy.health -= 20
        if enemy.health < 0:
            enemy.health = 0
        self.health += 10
        print(self.name, "бьет", enemy.name)
        print('%s = %d' % (enemy.name, enemy.health))

class Battle:

    def init(self, u1, u2):
        self.u1 = u1
        self.u2 = u2
        self.result = "Сражения не было"

    def battle(self):
        while self.u1.health > 0 and self.u2.health > 0:
            n = randint(1, 2)
            if n == 1:
                self.u1.make_kick(self.u2)
            else:
                self.u2.make_kick(self.u1)
        if self.u1.health > self.u2.health:
            self.result = self.u1.name + " ПОБЕДИЛ"
        elif self.u2.health > self.u1.health:
            self.result = self.u2.name + " ПОБЕДИЛ"

    def who_win(self):
        print(self.result)

first = Soldier('Mr. First',140)
second = Soldier()
second.set_name('Mr. Second')
b = Battle(first, second)
b.battle()
b.who_win()

import time
import random;
class Card():

    NumsList = ["Джокер", '2', '3', '4', '5', '6', '7', '8', '9', '10',
                "Валет", "Дама", "Король", "Туз"]
    MastList = ["пик", "крестей", "бубей", "червей"]

    def init(self, i, j):
        self.Mastb = self.MastList[i - 1];
        self.Num = self.NumsList[j - 1];

class DeckOfCards():

    def init(self):
        self.deck = [None] * 56;
        k = 0;
        for i in range(1, 4 + 1):
            for j in range(1, 14 + 1):
                self.deck[k] = Card(i, j);
                k += 1;


def shuffle(self):
        random.shuffle(self.deck);
        def get(self, i):
            if 0 <= i <=55:
                answer = self.deck[i].Num;
                answer += " ";
                answer += self.deck[i].Mastb;
            else:
                answer = "В колоде только 56 карт"
            return answer;

deck = DeckOfCards();
deck.shuffle();
print('Выберите карту из колоды в 56 карт:');
n=int(input())
if n<=56 :
 card = deck.get(n-1);
 print('Вы взяли карту: ', card, end='.\n');
else :
 print("В колоде только 56 карт")

class Vector3D:

    def init(self, x, y, z):
        self.coords = (x, y, z)

    def display(self):
        print(f"Vector3D: {self.coords}")

class method:

    def read(cls):
        x, y, z = map(int, input("Введите координаты: ").split())
        return cls(x, y, z)

    def add(self, other):
      if isinstance(other, Vector3D):
        return Vector3D(self.coords[0] + other.coords[0], self.coords[1] + other.coords[1], self.coords[2] + other.coords[2])
      else:
        raise TypeError("Можно добавить только два экземпляра Vector3D или экземпляры с совместимыми координатами.")

    def sub(self, other):
        return self + (-other)

def mul(self, factor):
    if factor == 0:
        raise ZeroDivisionError("Невозможно разделить на ноль")

class RectTriangle:

    def init(self, a, b):
        self.a = a
        self.b = b

    def increase_side(self, percent):
        new_a = (self.a * (100 + percent)) // 100
        new_b = (self.b * (100 + percent)) // 100
        return RectTriangle(new_a, new_b)

    def decrease_side(self, percent):
        new_a = self.a - (self.a * percent) // 100
        new_b = self.b - (self.b * percent) // 100
        if new_a < 0 or new_b < 0:
            raise ValueError("Side cannot become negative.")
        return RectTriangle(new_a, new_b)

    def calc_circumcircle_radius(self):
        a, b = self.a, self.b

class Bus:

    def init(self, speed, capacity, seats):
        self.speed = speed
        self.capacity = capacity
        self.maxSpeed = maxSpeed
        self.passengers = []
        self.hasEmptySeats = True
        self.seats = seats

    def addPassenger(self, passenger):
        self.passengers.append(passenger)

    def removePassenger(self, passenger):
        self.passengers.remove(passenger)

    def setSpeed(self, newSpeed):
        if newSpeed >= 0 and newSpeed <= self.maxSpeed:
            self.speed = newSpeed
        else:
            print("Invalid speed.")