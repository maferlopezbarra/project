from src.processors import displacements


def test_displacements():
    assert displacements([("A10", "15500")], 10300, 250) == [
        {"node": "A10", "drift": 21}
    ]
    assert displacements([("AB100", "10000")], 10300, 250) == [
        {"node": "AB100", "drift": 0}
    ]


def test_blankline():
    assert displacements([("A10", "15500"), ""], 10300, 250) == [
        {"node": "A10", "drift": 21}
    ]
