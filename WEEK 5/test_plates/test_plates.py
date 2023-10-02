from plates import is_valid

def test_lengthbelow():
    assert is_valid("a") == False


def test_lengthover():
    assert is_valid("abcdefghjk") == False


def test_punct():
    assert is_valid("CS.") == False

def test_digit():
    assert is_valid("CS05") == False

def test_beginning_alphabetical_checks():
    assert is_valid("22") == False
    assert is_valid("2A") == False
    assert is_valid("A2") == False
    assert is_valid("PO") == True

def test_placement():
    assert is_valid("CS50") == True
    assert is_valid("CS50P2") == False


