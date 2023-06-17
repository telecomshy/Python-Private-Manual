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


class HeroFactory:
    hero_map = {'ironman': IronMan, 'spiderman': SpiderMan}

    def create_hero(self, hero_choice):
        return self.hero_map[hero_choice.lower()]()


class WeaponFactory:
    weapon_map = {'armour': Armour, 'shooter': Shooter}

    def create_weapon(self, weapon_choice):
        return self.weapon_map[weapon_choice.lower()]()
