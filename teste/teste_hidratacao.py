import pytest

from app.hidratacao import calculo_hidratacao

def test_hidratacao_base():
    assert calculo_hidratacao(70, 20) == 2.45

def test_hidratacao_dia_quente():
    assert calculo_hidratacao(70,32) == 3.15

def test_hidratacao_dia_ameno():
    assert calculo_hidratacao(70, 27) == 2.8

def test_peso_invalido():
    with pytest.raises(ValueError):
        calculo_hidratacao(0, 20)