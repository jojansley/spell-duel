class Spell:
    def __init__(self, name, spell_type, power):
        self.name = name
        self.spell_type = spell_type
        self.power = power


class SpellBook:
    def __init__(self):
        self.spells = [Spell("Incendio", "damage", 25), Spell("Episkey", "heal", 20), Spell("Protego", "shield", 0)]

    def choose_spell_by_die(self, roll):
        # roll is expected to be 1-based (1, 2, or 3)
        if 1 <= roll <= len(self.spells):
            return self.spells[roll - 1]
        raise ValueError("Invalid die roll")
