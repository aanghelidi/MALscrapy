from typing import Union


def get_last_split_value(s: str, sep: str) -> str:
    return s.split(sep=sep, maxsplit=1)[-1]


def parse_int_or_value(v: str) -> Union[str, int]:
    try:
        return int(v)
    except ValueError as e:
        print(e)
    return v


def remove_comma(s: str) -> str:
    return s.replace(",", "")
