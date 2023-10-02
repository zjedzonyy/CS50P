from bank import value

def main():
    test_ishello()
    test_ish()
    test_noh()

def test_ishello():
    assert value("hello") == 0

def test_ish():
    assert value("hi") == 20

def test_noh():
    assert value("good morning, sir") == 100

def test_case():
    assert value("Hello") == 0

if __name__ == "__main__":
    main()