from tld import *

def test_tld():
    assert tld("georgetown.edu") == "edu"
    assert tld("www.google.com") == "com"
    assert tld("nope") == "nope"

    print(tld("georgetown.edu"))
    print(tld("www.google.com"))
    print(tld("nope"))

test_tld()