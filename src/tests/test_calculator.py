"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition():
    calc = Calculator()
    assert calc.addition(2, 3) == 5

def test_subtraction():
    calc = Calculator()
    assert calc.subtraction(10, 4) == 6

def test_multiplication():
    calc = Calculator()
    assert calc.multiplication(4, 5) == 20

def test_division():
    calc = Calculator()
    assert calc.division(10, 2) == 5

def test_division_by_zero():
    calc = Calculator()
    assert calc.division(10, 0) == "Erreur : division par zéro"

"""def test_addition_fail():
    calc = Calculator()
    assert calc.addition(2, 3) == 6  # Faux résultat """