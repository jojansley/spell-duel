from wizards import Wizard
from spells import SpellBook
from engine import GameEngine


def test_game_engine_initialization():
    wizard1 = Wizard("Harry", 100)
    wizard2 = Wizard("Draco", 100)
    spellbook = SpellBook()
    engine = GameEngine(wizard1, wizard2, spellbook)
    assert engine.wizard1.name == "Harry"
    assert engine.wizard2.name == "Draco"
    assert isinstance(engine.spellbook, SpellBook)


def test_ai_spell_choice():
    from spells import SpellBook

    spellbook = SpellBook()
    engine = GameEngine(Wizard("Player", 100), Wizard("Computer", 100), spellbook)
    ai = engine.wizard2

    # When AI health > 50, should choose either attack or shield (randomly)
    ai.health = 80
    spell = engine.choose_ai_spell(ai)
    assert spell.spell_type in ("damage", "shield")

    # When AI health <= 50, should choose heal (with some randomness, but always possible)
    ai.health = 50
    heal_found = False
    # Try several times to account for randomness
    for _ in range(10):
        spell = engine.choose_ai_spell(ai)
        if spell.spell_type == "heal":
            heal_found = True
            break
    assert heal_found, "AI should choose heal when health <= 50"

    ai.health = 30
    heal_found = False
    for _ in range(10):
        spell = engine.choose_ai_spell(ai)
        if spell.spell_type == "heal":
            heal_found = True
            break
    assert heal_found, "AI should choose heal when health <= 50"