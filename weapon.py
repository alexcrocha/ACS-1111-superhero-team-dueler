import random

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self):
        """_summary_: This method returns a random value
            between one half to the full attack power of the weapon.
        """
        return random.randint(self.damage // 2, self.damage)

