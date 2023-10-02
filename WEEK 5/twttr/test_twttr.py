from twttr import shorten

def main():
    test_twttr_lowercase()
    test_twttr_capitalized()
    test_twttr_numbers()
    test_twttr_punct()

def test_twttr_lowercase():
    assert shorten("twitter") == "twttr"

def test_twttr_capitalized():
    assert shorten("CAt") == "Ct"

def test_twttr_numbers():
    assert shorten("d0g") == "d0g"

def test_twttr_punct():
    assert shorten(",.") == ",."

if __name__ == "__main__":
    main()