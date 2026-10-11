"""Defines tests for the StdUnc class."""

import itertools

import pytest
from uncertainties import ufloat

from unc import StdUnc

CASES = ((10, 1), (10, 2), (20, 0.1), (10, 0.1), (0.1234, 0.02))
pairs = pytest.mark.parametrize("ab", list(itertools.permutations(CASES, 2)))


@pairs
def test_add(ab):
    """Test addition of two StdUnc instances."""
    a, b = ab
    assert StdUnc(*a) + StdUnc(*b) == ufloat(*a) + ufloat(*b)


@pairs
def test_sub(ab):
    """Test subtraction between two StdUnc instances."""
    a, b = ab
    assert StdUnc(*a) - StdUnc(*b) == ufloat(*a) - ufloat(*b)


@pairs
def test_mul(ab):
    """Test multiplication between two StdUnc instances."""
    a, b = ab
    assert StdUnc(*a) * StdUnc(*b) == ufloat(*a) * ufloat(*b)


@pairs
def test_div(ab):
    """Test division of two StdUnc instances."""
    a, b = ab
    assert StdUnc(*a) / StdUnc(*b) == ufloat(*a) / ufloat(*b)
