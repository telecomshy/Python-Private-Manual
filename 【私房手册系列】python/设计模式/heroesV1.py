from abc import ABC, abstractmethod


class Hero(ABC):
    @abstractmethod
    def attack(self):
        pass

    def equip(self, weapon):
        self.weapon = weapon


class IronMan(Hero):
    def attack(self):
        print(f"钢铁侠用{self.weapon}发起攻击！")


class SpiderMan(Hero):
    def attack(self):
        print(f"蜘蛛侠用{self.weapon}发起攻击！")


class Weapon(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Armour(Weapon):
    def __str__(self):
        return "战甲"


class Shooter(Weapon):
    def __str__(self):
        return "蛛丝发射器"
