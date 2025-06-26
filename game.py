import random
import time

from termcolor import colored

from engine import GameEngine
from spells import SpellBook
from wizards import Wizard

# spell-duel/game.py
# This is the main game loop for the Spell Duel game.
# It initializes the wizards, spellbook, and game engine,
# and manages the turns of the duel.

# Possible colors to be passed to termcolor.colored: 'grey','red','green','yellow','blue','magenta','cyan','white'


def main():
    print("Welcome to Spell Duel!")
    mode = ""
    while mode not in ["1", "2"]:
        mode = input("Choose mode:(1) Player vs Computer, (2) Player vs Player: ").strip()

    name1 = input("Enter name for Player 1: ").strip() or "Player 1"
    if mode == "2":
        name2 = input("Enter name for Player 2: ").strip() or "Player 2"
    else:
        name2 = "Computer"

    wizard1 = Wizard(name1, 100)
    wizard2 = Wizard(name2, 100)
    spellbook = SpellBook()
    engine = GameEngine(wizard1, wizard2, spellbook)

    current_wizard = wizard1
    opponent = wizard2

    while wizard1.health > 0 and wizard2.health > 0:
        print(f"\n{current_wizard.name}'s turn!")
        if mode == "1" and current_wizard == wizard2:
            spell = engine.choose_ai_spell(current_wizard)
            roll = random.randint(1, 5)
            print("Computer is thinking...")
            time.sleep(1)
            print(f"Computer rolled {roll} and casts {spell.name}!")
        else:
            print("Choose a spell:")
            for i, s in enumerate(spellbook.spells, 1):
                print(f"{i}: {s.name} ({s.spell_type}, Power: {s.power})")
            while True:
                try:
                    spell_choice = int(input("Enter spell number (1-3): "))
                    spell = spellbook.choose_spell_by_die(spell_choice)
                    roll = random.randint(1, 5)
                    break
                except Exception:
                    print("Invalid choice. Please enter 1, 2, or 3.")

            print(f"{current_wizard.name} casts {spell.name} (rolls {roll})!")

        engine.apply_spell(current_wizard, opponent, spell, die_roll=roll)

        print()
        print(f"{wizard1.name} Health: {int(round(wizard1.health))}")
        if wizard1.active_shield > 0:
            shield_str = f"{wizard1.name} Shield: {int(wizard1.active_shield * 100)}%"
            print(colored(shield_str, "blue"))
        print(f"{wizard2.name} Health: {int(round(wizard2.health))}")
        if wizard2.active_shield > 0:
            shield_str = f"{wizard1.name} Shield: {int(wizard1.active_shield * 100)}%"
            print(colored(shield_str, "blue"))

        current_wizard, opponent = opponent, current_wizard

    winner = wizard1 if wizard1.health > 0 else wizard2
    print(f"\n{winner.name} wins the duel!")


if __name__ == "__main__":
    main()
