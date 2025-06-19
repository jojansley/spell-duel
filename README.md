

---

# Spell Duel: Dev Branch Coding Guide (TDD Edition)

Welcome wizard-in-training! You're now ready to begin actual coding on the `dev` branch of the **Spell Duel: Hogwarts Edition** project. You'll be practicing **Test-Driven Development (TDD)**, which means:

>**Write the test first**, make it **fail**, then **write the code to pass** it.

Below is your detailed guide, broken into clear steps, with **at least 1 hour of work** lined up.

---

##  Step 1: Write Your First Test (`test_spells.py`)

You're going to begin by writing a test for the `Spell` class.

Create or open the file:

```bash
code test_spells.py
```

Then write this test:

```python
from spells import Spell

def test_spell_initialization():
    spell = Spell("Incendio", "damage", 25)
    assert spell.name == "Incendio"
    assert spell.spell_type == "damage"
    assert spell.power == 25
```

> Don’t write the class yet! This is your **failing test first** step.

---

## Step 2: Run the Test and Watch It Fail

In your terminal:

```bash
pytest
```

You should see an `ImportError` or `NameError` — that’s good! It means your test is being picked up and it's failing as expected.

---

## Step 3: Write the Minimum Code to Pass the Test

Create the `Spell` class in `spells.py`:

```python
class Spell:
    def __init__(self, name, spell_type, power):
        self.name = name
        self.spell_type = spell_type
        self.power = power
```

Re-run your test:

```bash
pytest
```

If it passes — you’ve completed your first TDD cycle!

---

## Step 4: Add More Tests for Spell Behavior

Add 2 more tests in `test_spells.py` to build confidence in your class design.

```python
def test_spell_is_damage_type():
    spell = Spell("Stupefy", "damage", 15)
    assert spell.spell_type == "damage"

def test_spell_with_zero_power():
    spell = Spell("Protego", "shield", 0)
    assert spell.power == 0
```

Then:

```bash
pytest
```

Stretch: Try using `pytest.param` or loops to test many spells at once.

---

## Step 5: Create a List of Sample Spells in `spells.py`

Below your `Spell` class, define some common spells as **instances**:

```python
Incendio = Spell("Incendio", "damage", 25)
Episkey = Spell("Episkey", "heal", 20)
Protego = Spell("Protego", "shield", 0)

spellbook = [Incendio, Episkey, Protego]
```

> You’ll use this `spellbook` in the game engine later.

Write a new test:

```python
def test_spellbook_contains_known_spells():
    from spells import spellbook
    assert len(spellbook) >= 3
    assert any(spell.name == "Episkey" for spell in spellbook)
```

---

## Step 6: Refactor for Style

Now do a cleanup pass:

```bash
black .
```

Optional:

```bash
flake8
```

Check that all tests still pass:

```bash
pytest
```

---

## Step 7: Commit Your Work

```bash
git add .
git commit -m "Add Spell class and spellbook with initial tests"
git push origin dev
```

---

## Stretch Task (Optional if You Finish Early)

### ➕ Add a `describe()` method to `Spell` class

In `spells.py`:

```python
def describe(self):
    return f"{self.name} ({self.spell_type}) – Power: {self.power}"
```

And test it:

```python
def test_spell_description():
    spell = Spell("Episkey", "heal", 20)
    assert "heal" in spell.describe()
```

---

## What You Should Understand After This Hour

By the end of this session, you’ll have practiced:

* Creating and testing a class from scratch
* Writing failing tests first (TDD)
* Using `pytest` assertions
* Organizing a test file and logic file cleanly
* Committing work to a development branch

---
