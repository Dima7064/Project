import re
VALID_CHARS = re.compile(r"^[А-ЯЁа-яё'\- ]+$")
MIN_LEN = 3
def normalize(name: str) -> str:
    name = name.strip().replace("’", "'").replace("‘", "'")
    name = re.sub(r"\s+", " ", name)
    if not VALID_CHARS.match(name):
        raise ValueError(f"Недопустимые символы: {name!r}")
    if len(name.replace(" ", "")) < MIN_LEN:
        raise ValueError(f"Слишком короткое: {name!r}")
    return " ".join(word.capitalize() for word in name.split())
