

def test_short_phrase():
    phrase = input("Set a phrase: ")
    assert len(phrase) < 15, f"The phrase is tooooo long"