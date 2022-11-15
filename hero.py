import random


class Hero:
    def __init__(self, name, starting_health=100):
        """Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        """
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        """Current Hero will take turns fighting the opponent hero passed in."""
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 1) randomly choose winner,
        # Hint: Look into random library, more specifically the choice method
        winner = random.choices(
            [self.name, opponent.name],
            weights=[
                self.current_health / (self.current_health + opponent.current_health),
                opponent.current_health / (self.current_health + opponent.current_health),
            ],
        )[0]
        loser = self.name if winner == opponent.name else opponent.name
        print(f"{winner} defeats {loser}!")


if __name__ == "__main__":
    hero1 = Hero("Brian Cahill", 300)
    hero2 = Hero("Josh Faigan", 250)

    hero1.fight(hero2)
