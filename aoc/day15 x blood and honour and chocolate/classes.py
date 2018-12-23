max_health = 200
attack_power = 3


class Unit:
    def __init__(self, species, location):
        self.spec = species
        self.loc = location
        self.hp = max_health
        self.atk = attack_power
        self.alive = True

    def __lt__(self, other):
        return self.loc[0] < other.loc[0] or\
            self.loc[0] == other.loc[0] and self.loc[1] < other.loc[1]

    def __repr__(self):
        return str(self.loc)+" "+self.spec+" "+str(self.hp)

    def die(self):
        self.alive = False
