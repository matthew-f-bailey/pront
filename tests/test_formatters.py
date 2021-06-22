import pytest

from pront.formatters import Formatter


@pytest.fixture
def input_list():
    my_list = ["foo", "bar", "baz"]
    return my_list


@pytest.fixture
def input_dict():
    my_dict = {
        "foo": 1,
        "bar": "string",
        "baz": ["list"]
    }
    return my_dict


def test_list_formatting(input_list):
    formatter = Formatter()
    formatted = formatter.format(input_list)

    expected = \
        f'Type: <list>\n' \
        f'[\n' \
        f'   "foo",\n' \
        f'   "bar",\n' \
        f'   "baz"\n' \
        ']'

    assert formatted == expected


def test_dict_formatting(input_dict):
    formatter = Formatter()
    formatted = formatter.format(input_dict)

    expected = \
        f"Type: <dict>\n" \
        "{" \
        f'\n   "foo": 1,\n' \
        f'   "bar": "string",\n' \
        f'   "baz": [\n' \
        f'      "list"\n' \
        f'   ]\n' \
        "}"
    assert formatted == expected