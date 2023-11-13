from pytest import capsys
from functions import say_hello

def test_say_hello(name):
    printed = capsys.readouterr()
    assert printed.out.split(' ')[1]==name

