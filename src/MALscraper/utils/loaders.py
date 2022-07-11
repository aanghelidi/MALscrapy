def get_last_split_value(s: str, sep: str) -> str:
    return s.split(sep=sep, maxsplit=1)[-1]
