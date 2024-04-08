#!/usr/bin/python
from calculator import *
import pytest

def test_lb2kg():
    assert lb2kg(125) == 56.25

def test_in2m():
    assert in2m(63) == 1.575

def test_calcBMI():
    assert calcBMI(1.575, 56.25) == 22.7

def test_bmiCategory():
    assert bmiCategory(18.4) == "Underweight"
    assert bmiCategory(18.5) == "Normal Weight"

    assert bmiCategory(24.9) == "Normal Weight"
    assert bmiCategory(25) == "Overweight"

    assert bmiCategory(29.9) == "Overweight"
    assert bmiCategory(30) == "Obese"
