from functions import say_hello


def test_say_hello(capsys):
    name = 'casa'
    say_hello(name)
    printed = capsys.readouterr()
    assert printed.out.split(' ')[1][:-1]==name.capitalize()

