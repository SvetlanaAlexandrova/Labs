class Human:
    default_name = 'Имя'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print('{0}, возраст - {1}, денег - {2} млн'.format(self.name, self.age, self.__money), end=', ')
        print('нет дома') if self.__house is None else print('дом {0}'.format(self.__house.info()))

    def earn_money(self, money):
        self.__money += money
        print('Вы заработали', self.__money, 'млн')

    def buy_house(self, house, discount):
        print('Покупка дома {0}, скидка - {1}%...'.format(house.info(), discount))
        if self.__money >= house.final_price(discount):
            self.__make_deal(house, discount)
        else:
            print('> У вас недостаточно средств')

    def __make_deal(self, house, discount):
        self.__money -= house.final_price(discount)
        self.__house = house
        print('> Вы купили дом!')

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age)


class House:
    def __init__(self, area=10, price=10):
        self.__area = area
        self.__price = price

    def final_price(self, discount=100):
        return self.__price * (100 - discount) / 100

    def info(self):
        return 'с площадью {0} м2, по цене {1} млн'.format(self.__area, self.__price)


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)


# 1. Метод default_info() для класса Human
Human.default_info()

# 2. Объект класса Human
hum = Human('Марк', 21)

# 3. Информация об объекте
hum.info()

# 4. Объект класса SmallHouse
building = SmallHouse(18)

# 5. Покупка дома
hum.buy_house(building, 5)

# 6. Получение заработка
hum.earn_money(40)

# 7. Покупка дома 2.0
hum.buy_house(building, 5)

# 8. Информация об объекте
hum.info()

