import pytest

from string_calculator import add

def test_empty_string_returns_zero():

    assert add("") == 0

def test_one_numbers():

    assert add("1") == 1

def test_two_numbers():

    assert add("1,2") == 3

def test_four_numbers():

    assert add("1,2,3,4") == 10

def test_with_newline():

    assert add("1\n2,3") == 6

def test_newline_at_end_errors():

    with pytest.raises(ValueError):
        add("1,\n")

def test_change_delimiter():

    assert add("//;\n1;2") == 3

def test_two_negative():

    with pytest.raises(Exception) as error:
        add("-1, -1")

    assert error.value.args[0] == "negatives not allowed: -1, -1"

def test_numbers_large_than_1000_should_be_ignored():

    assert add("1001, 2") == 2

def test_any_length_delimieter():

    assert add("//[***]\n1***2***3") == 6

def test_allow_multiple_delimiters():

    assert ("//[*][%]\n1*2%3") == 6