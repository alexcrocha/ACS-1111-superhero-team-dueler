from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team


class Arena:
    def __init__(self):
        """Instantiate properties
        team_one: None
        team_two: None
        """
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        """Prompt for Ability information.
        reutrn Ability with values from user Input
        """
        name = input("What is the ability name? > ")
        max_damage = int(input("What is the max damage of the ability? > "))

        return Ability(name, max_damage)

    def create_weapon(self):
        """Prompt user for Weapon information
        return Weapon with values from user input.
        """
        name = input("What is the weapon name? > ")
        max_damage = int(input("What is the max damage of the weapon? > "))

        return Weapon(name, max_damage)

    def create_armor(self):
        """Prompt user for Armor information
        return Armor with values from user input.
        """
        name = input("What is the armor name? > ")
        max_block = int(input("What is the max block of the armor? > "))

        return Armor(name, max_block)

    def create_hero(self):
        """Prompt user for Hero information
        return Hero with values from user input.
        """
        hero_name = input("What is the hero's name? > ")
        hero = Hero(hero_name)
        choice = None
        while choice != "4":
            choice = input(
                "[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice > "
            )
            if choice == "1":
                hero.add_ability(self.create_ability())
            elif choice == "2":
                hero.add_weapon(self.create_weapon())
            elif choice == "3":
                hero.add_armor(self.create_armor())
            elif choice != "4":
                print("Oops, I don't recognize that. Please try again.")
        return hero

    def build_team_one(self):
        """Prompt the user to build team_one"""
        self.team_one = Team(input("What is the name of Team One? > "))
        numOfTeamMembers = int(
            input(f"How many members would you like on {self.team_one.name}? > ")
        )
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        """Prompt the user to build team_two"""
        self.team_two = Team(input("What is the name of Team Two? > "))
        numOfTeamMembers = int(
            input(f"How many members would you like on {self.team_two.name}? > ")
        )
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        """Battle team_one and team_two together."""
        self.team_one.attack(self.team_two)

    def show_stats(self):
        """Prints team statistics to terminal."""

        def show_team_stats(team):
            print(f"\n{team.name} statistics: ")
            team.stats()

        def show_kd_ratio(team):
            """Calculate the average number of kills/deaths for a team's heroes."""
            team_kills = 0
            team_deaths = 0
            for hero in team.heroes:
                team_kills += hero.kills
                team_deaths += hero.deaths
            if team_deaths == 0:
                team_deaths = 1
            print(
                f"{team.name} average K/D was: {str(team_kills / team_deaths if team_kills > 0 else 0)}"
            )

        def calculate_survivors(team):
            """Print surviving heroes."""
            num_alive = 0
            for hero in team.heroes:
                if hero.is_alive():
                    num_alive += 1
                    print(f"\nSurvived from {team.name}: {hero.name}")
            return num_alive

        team_one_survivors = calculate_survivors(self.team_one)
        team_two_survivors = calculate_survivors(self.team_two)

        def declare_winner(team_one_alive_count, team_two_alive_count):
            """Declare winning team."""
            if team_one_alive_count > team_two_alive_count:
                print(f"\n{self.team_one.name} won!")
            else:
                print(f"\n{self.team_two.name} won!")

        show_team_stats(self.team_one)
        show_kd_ratio(self.team_one)
        show_team_stats(self.team_two)
        show_kd_ratio(self.team_two)

        declare_winner(team_one_survivors, team_two_survivors)


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
