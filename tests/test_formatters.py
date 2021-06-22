import pytest

from pront.formatters import ListFormatter, DictFormatter


@pytest.fixture
def input_list():
    my_list = ["foo", "bar", "baz"]
    return my_list

def test_list_formatting(input_list):
    formatter = ListFormatter()
    formatted = formatter.format(input_list)
    expected = \
    "input_list\n" \
    "|0|foo|\n" \
    "|1|bar|\n" \
    "|2|baz|"

    assert formatted == expected