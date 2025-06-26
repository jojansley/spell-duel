from termcolor import colored

from engine import GameEngine
from spells import SpellBook
from wizards import Wizard


def test_full_duel_player1_wins():
    wizard1 = Wizard("Harry", 100)
    wizard2 = Wizard("Draco", 25)
    spellbook = SpellBook()
    engine = GameEngine(wizard1, wizard2, spellbook)
    # Harry casts Incendio (25 damage) on Draco
    spell = spellbook.choose_spell_by_die(1)
    engine.apply_spell(wizard1, wizard2, spell)
    assert wizard2.health == 0
    assert wizard1.health == 100


def test_heal_spell_increases_health():
    wizard1 = Wizard("Hermione", 50)
    wizard2 = Wizard("Voldemort", 100)
    spellbook = SpellBook()
    engine = GameEngine(wizard1, wizard2, spellbook)
    # Hermione casts Episkey (heal 20)
    spell = spellbook.choose_spell_by_die(2)
    engine.apply_spell(wizard1, wizard2, spell)
    assert wizard1.health == 70


def test_shield_spell_colors_terminal():
    wizard1 = Wizard("Luna", 80)
    wizard2 = Wizard("Bellatrix", 80)
    spellbook = SpellBook()
    engine = GameEngine(wizard1, wizard2, spellbook)
    # Luna casts Protego (shield, does nothing)
    spell = spellbook.choose_spell_by_die(3)
    engine.apply_spell(caster=wizard1, target=wizard2, spell=spell, die_roll=5)  # simulate rolling a 5 for test

    # Check Wizard active shield
    assert wizard1.active_shield > 0
    if wizard1.active_shield > 0:
        shield_str = f"Wizard 1 has an active shield of {wizard1.active_shield * 100}%"
        print(colored(shield_str, "blue"))


def test_health_never_negative():
    wizard1 = Wizard("Neville", 100)
    wizard2 = Wizard("Snape", 10)
    spellbook = SpellBook()
    engine = GameEngine(wizard1, wizard2, spellbook)
    # Neville casts Incendio (25 damage) on Snape (only 10 health)
    spell = spellbook.choose_spell_by_die(1)
    engine.apply_spell(wizard1, wizard2, spell)
    assert wizard2.health == 0
    assert wizard1.health == 100


test_shield_spell_colors_terminal()
