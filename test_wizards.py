from wizards import Wizard


def test_wizard_initialization():
    wizard = Wizard("Harry", 100)
    assert wizard.name == "Harry"
    assert wizard.health == 100
