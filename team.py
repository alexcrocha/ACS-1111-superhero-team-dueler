class Team:
    def __init__(self, name):
        """Initialize your team with its team name and a list of heroes"""
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        """Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True

        if not foundHero:
            return 0

    def view_all_heroes(self):
        """Prints out all heroes to the console"""
        # TODO: Loop over the list of heroes and print their names to the terminal one by one.
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        """Add Hero object to self.heroes."""
        self.heroes.append(hero)
