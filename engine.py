import random


class GameEngine:
    def __init__(self, wizard1, wizard2, spellbook):
        self.wizard1 = wizard1
        self.wizard2 = wizard2
        self.spellbook = spellbook

    def apply_spell(self, caster, target, spell, die_roll=None):
        attack_mod = {1: -15, 2: -10, 3: 0, 4: 5, 5: 10}
        heal_mod = {1: -10, 2: -5, 3: 0, 4: 5, 5: 10}
        shield_mod = {1: 0.1, 2: 0.2, 3: 0.4, 4: 0.8}
        max_health = 100

        if spell.spell_type == "shield":
            # Store shield effect on the caster for next attack
            if die_roll in shield_mod:
                caster.active_shield = shield_mod[die_roll]
            else:
                caster.active_shield = 0
            return

        if spell.spell_type == "damage":
            power = spell.power
            if die_roll is not None:
                power += attack_mod.get(die_roll, 0)
            # Check if target has shield
            shield = getattr(target, "active_shield", 0)
            if shield:
                power = power * (1 - shield)
                target.active_shield = 0  # Shield is used up after one attack
            target.health -= power
            if target.health < 0:
                target.health = 0

        elif spell.spell_type == "heal":
            power = spell.power
            if die_roll is not None:
                power += heal_mod.get(die_roll, 0)
            caster.health += power
            if caster.health > max_health:
                caster.health = max_health

    def choose_ai_spell(self, ai_wizard):
        # AI chooses heal if health <= 50, else randomly attack or shield
        spells = [spell for spell in self.spellbook.spells]
        if ai_wizard.health <= 50:
            heal_spells = [s for s in spells if s.spell_type == "heal"]
            return random.choice(heal_spells)
        else:
            attack_or_shield = [s for s in spells if s.spell_type in ("damage", "shield")]
            return random.choice(attack_or_shield)
