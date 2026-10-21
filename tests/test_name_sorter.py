import pytest
from name_sorter import NameSorter


def test_sorter_orders_primarily_by_last_name():
    sorter = NameSorter()
    raw_names = [
        "Shayan Ghalehdar",
        "Marin Alvarez",
        "Beau Bentley",
    ]
    expected = [
        "Marin Alvarez",
        "Beau Bentley",
        "Shayan Ghalehdar",
    ]
    assert sorter.sort(raw_names) == expected


def test_sorter_tie_breaks_using_given_names():
    sorter = NameSorter()
    raw_names = [
        "Shayan Reza Ghalehdar",
        "Kaveh Ghalehdar",
        "Shayan Darius Ghalehdar",
        "Babak Ghalehdar",
    ]
    expected = [
        "Babak Ghalehdar",
        "Kaveh Ghalehdar",
        "Shayan Darius Ghalehdar",
        "Shayan Reza Ghalehdar",
    ]
    assert sorter.sort(raw_names) == expected


def test_sorter_tie_breaks_shorter_prefix():
    """A person with fewer given names precedes one with more if shared tokens match."""
    sorter = NameSorter()
    raw_names = [
        "Shayan Reza Ghalehdar",
        "Shayan Ghalehdar",
    ]
    expected = [
        "Shayan Ghalehdar",
        "Shayan Reza Ghalehdar",
    ]
    assert sorter.sort(raw_names) == expected


def test_sorter_ignores_blank_lines():
    sorter = NameSorter()
    raw_names = [
        "Shayan Ghalehdar",
        "",
        "   ",
        "Marin Alvarez",
    ]
    expected = [
        "Marin Alvarez",
        "Shayan Ghalehdar",
    ]
    assert sorter.sort(raw_names) == expected


def test_sorter_empty_input():
    sorter = NameSorter()
    assert sorter.sort([]) == []


def test_sorter_propagates_invalid_name_error():
    sorter = NameSorter()
    with pytest.raises(ValueError):
        sorter.sort(["Shayan Ghalehdar", "Madonna"])