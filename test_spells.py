# -*- coding: utf-8 -*-

from engine import GameEngine
from spells import Spell, SpellBook
from wizards import Wizard


def test_choose_spell_by_die():
    spellbook = SpellBook()
    # Simulate die rolls 1, 2, 3
    assert spellbook.choose_spell_by_die(1).name == "Incendio"
    assert spellbook.choose_spell_by_die(2).name == "Episkey"
    assert spellbook.choose_spell_by_die(3).name == "Protego"


def test_heal_does_not_exceed_max_health():
    wizard = Wizard("Test", 95)
    spell = Spell("Episkey", "heal", 10)
    engine = GameEngine(wizard, Wizard("Dummy", 100), SpellBook())
    engine.apply_spell(wizard, None, spell)
    assert wizard.health == 100  # Should not exceed max health


def test_damage_does_not_go_below_zero():
    wizard = Wizard("Test", 5)
    spell = Spell("Incendio", "damage", 10)
    engine = GameEngine(Wizard("Dummy", 100), wizard, SpellBook())
    engine.apply_spell(engine.wizard1, wizard, spell)
    assert wizard.health == 0  # Should not go below zero


def test_attack_multiplier_by_die_roll():
    # Example multipliers: 1=-15, 2=-10, 3=0, 4=+5, 5=+10 (base 25)
    base_power = 25
    multipliers = {1: -15, 2: -10, 3: 0, 4: 5, 5: 10}
    for roll, mod in multipliers.items():
        wizard = Wizard("Target", 100)
        spell = Spell("Incendio", "damage", base_power)
        engine = GameEngine(Wizard("Caster", 100), wizard, SpellBook())
        engine.apply_spell(engine.wizard1, wizard, spell, die_roll=roll)
        expected = 100 - (base_power + mod)
        if expected < 0:
            expected = 0
        assert wizard.health == expected


def test_heal_multiplier_by_die_roll():
    # Example multipliers: 1=-10, 2=-5, 3=0, 4=+5, 5=+10 (base 20)
    base_power = 20
    multipliers = {1: -10, 2: -5, 3: 0, 4: 5, 5: 10}
    for roll, mod in multipliers.items():
        wizard = Wizard("Healer", 80)
        spell = Spell("Episkey", "heal", base_power)
        engine = GameEngine(wizard, Wizard("Dummy", 100), SpellBook())
        engine.apply_spell(wizard, None, spell, die_roll=roll)
        expected = 80 + base_power + mod
        if expected > 100:
            expected = 100
        assert wizard.health == expected


def test_shield_reduces_damage_by_multiplier():
    # Shield multipliers: 1=10%, 2=20%, 3=40%, 4=80%
    shield_multipliers = {1: 0.1, 2: 0.2, 3: 0.4, 4: 0.8}
    base_attack = 25
    for roll, reduction in shield_multipliers.items():
        attacker = Wizard("Attacker", 100)
        defender = Wizard("Defender", 100)
        spellbook = SpellBook()
        engine = GameEngine(attacker, defender, spellbook)
        # Defender casts shield
        engine.apply_spell(defender, None, Spell("Protego", "shield", 0), die_roll=roll)
        # Store shield effect on defender
        defender.active_shield = reduction
        # Attacker casts attack
        engine.apply_spell(attacker, defender, Spell("Incendio", "damage", base_attack), die_roll=3)
        # Calculate expected damage after shield
        expected_damage = base_attack * (1 - reduction)
        expected_health = 100 - expected_damage
        assert defender.health == expected_health
