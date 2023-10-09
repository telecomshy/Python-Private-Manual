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


class Hawkeye(Hero):
    def attack(self):
        print(f"鹰眼用{self.weapon}发起攻击！")


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


class Arrow(Weapon):
    def __str__(self):
        return "弓箭"


class HeroFactory(ABC):
    @abstractmethod
    def create_hero(self):
        pass

    def create_weapon(self):
        pass


class IronmanFactory(HeroFactory):
    def create_hero(self):
        hero = IronMan()
        return hero

    def create_weapon(self):
        weapon = Armour()
        return weapon


class SpidermanFactory(HeroFactory):
    def create_hero(self):
        hero = SpiderMan()
        return hero

    def create_weapon(self):
        weapon = Shooter()
        return weapon


class HawkeyeFactory(HeroFactory):
    def create_hero(self):
        hero = Hawkeye()
        return hero

    def create_weapon(self):
        weapon = Arrow()
        return weapon


class HeroAbstractFactory:
    map_ = {
        'ironman': IronmanFactory,
        'spiderman': SpidermanFactory,
        'hawkeye': HawkeyeFactory
    }

    def get_herofactory(self, choice):
        return self.map_[choice.lower()]()
