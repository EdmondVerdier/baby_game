from random import randint

from src.constants import MATCH_PHOTOS


def pop_sicariot() -> dict[str, str]:
    roll = randint(0, len(MATCH_PHOTOS) - 1)
    sicariot = MATCH_PHOTOS[roll]
    return sicariot
