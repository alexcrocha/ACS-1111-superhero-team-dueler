import random
from ability import Ability
from armor import Armor


class Hero:
    def __init__(self, name, starting_health=100):
        """Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        """
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        """Current Hero will take turns fighting the opponent hero passed in."""
        if (len(self.abilities) == 0) and (len(opponent.abilities) == 0):
            print(f"{self.name} and {opponent.name} are not in the mood to fight right now.")
        else:
            while self.is_alive() and opponent.is_alive():
                opponent.take_damage(self.attack())
                if opponent.is_alive() == False:
                    print(f"{self.name} defeats {opponent.name}!")
                    break
                self.take_damage(opponent.attack())
                if self.is_alive() == False:
                    print(f"{opponent.name} defeats {self.name}!")
                    break


    def add_ability(self, ability):
        """Add ability to abilities list."""
        self.abilities.append(ability)

    def attack(self):
        """_summary_: Calculate the total damage from all ability attacks.
        return: total: Integer
        """

        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        """ Add armor to self.armors
            Armor: Armor Object
        """
        self.armors.append(armor)

    def defend(self):
        """_summary_: Calculate the total block amount from all armor blocks.
        return: total_block:Int
        """
        total_armor = 0
        for armor in self.armors:
            total_armor += armor.block()
        return total_armor

    def take_damage(self, damage):
        """_summary_: Updates self.current_health to reflect the damage minus the defense.
        """
        mitigation = self.defend()
        self.current_health -= damage - mitigation if damage - mitigation > 0 else 0

    def is_alive(self):
        """_summary_: Return True or False depending on whether the hero is alive or not.
        """
        return True if self.current_health > 0 else False

if __name__ == "__main__":
    hero1 = Hero("Brian Cahill", 300)
    hero2 = Hero("Josh Faigan", 250)
    ability1 = Ability("Super Eyes", 130)
    ability2 = Ability("Super Speed", 230)
    armor1 = Armor("Wizard Pointy Hat", 80)
    armor2 = Armor("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_armor(armor1)
    hero2.add_ability(ability2)
    hero2.add_armor(armor2)
    hero1.fight(hero2)
