import pytest

from ..utils.loaders import get_last_split_value


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
