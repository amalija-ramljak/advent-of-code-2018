class Group:
    def __init__(self, spec, count, health, initiative, damage, dmg_type, immunity=None, weakness=None):
        self.spec = spec
        self.count = count
        self.health = health
        self.initiative = initiative
        self.damage = [damage, dmg_type]
        self.immunity = immunity
        self.weakness = weakness

    def __repr__(self):
        return self.spec + " " + str(self.count) + " " + str(self.health)

    def __lt__(self, other):
        self_effective = self.damage[0]*self.count
        other_effective = other.damage[0]*other.count
        return self_effective > other_effective or\
            self_effective == other_effective and self.initiative > other.initiative
