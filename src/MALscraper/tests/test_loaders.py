import pytest

from ..utils.loaders import get_last_split_value, parse_int_or_value


@pytest.mark.parametrize(
    "field,sep,expected",
    [
        ("foo|bar", "|", "bar"),
        ("foo:bar", ":", "bar"),
        ("foo bar", " ", "bar"),
        ("foobar", ",", "foobar"),
    ],
)
def test_last_split_value(field, sep, expected):
    actual = get_last_split_value(field, sep)
    assert actual == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ("1", 1),
        ("2.3", "2.3"),
        ("foo bar", "foo bar"),
    ],
)
def test_parse_int_or_value(value, expected):
    actual = parse_int_or_value(value)
    assert actual == expected
