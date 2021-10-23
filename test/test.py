from main import obter_int

def test_obter_int():
    assert int == type(obter_int("Digite um número:"))

#python -m pytest .\test\test.py -s