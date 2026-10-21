import pytest
from name_sorter import Name


def test_name_with_one_given_name():
    person = Name("Shayan Ghalehdar")
    assert person.last_name == "Ghalehdar"
    assert person.given_names == ["Shayan"]
    assert str(person) == "Shayan Ghalehdar"


def test_name_with_two_given_names():
    person = Name("Shayan Reza Ghalehdar")
    assert person.last_name == "Ghalehdar"
    assert person.given_names == ["Shayan", "Reza"]
    assert str(person) == "Shayan Reza Ghalehdar"


def test_name_with_three_given_names():
    person = Name("Shayan Reza Darius Ghalehdar")
    assert person.last_name == "Ghalehdar"
    assert person.given_names == ["Shayan", "Reza", "Darius"]
    assert str(person) == "Shayan Reza Darius Ghalehdar"


def test_no_given_name_fails():
    with pytest.raises(ValueError, match="at least 1 given name"):
        Name("Shayan")


def test_more_than_three_given_names_fails():
    with pytest.raises(ValueError, match="at most 3 given names"):
        Name("Shayan Junior P. Schneider Ghalehdar")


def test_empty_and_whitespace_only_names_fail():
    with pytest.raises(ValueError):
        Name("")
    with pytest.raises(ValueError):
        Name("   ")


def test_handling_irregular_whitespace():
    person = Name("   Shayan    Reza   Ghalehdar   ")
    assert person.last_name == "Ghalehdar"
    assert person.given_names == ["Shayan", "Reza"]
    assert str(person) == "Shayan Reza Ghalehdar"


def test_name_sort_key():
    person = Name("Shayan Reza Ghalehdar")
    assert person.sort_key == ("Ghalehdar", ["Shayan", "Reza"])