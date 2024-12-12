import pytest

from src.generators import card_number_generator


def test_card_number_generator_standard(card_number_generator_fixture):
    assert list(card_number_generator(1, 5)) == card_number_generator_fixture


@pytest.mark.parametrize("start, finish, expected", [(2, 3, ["0000 0000 0000 0002"])])
def test_card_number_generator(start, finish, expected):
    assert list(card_number_generator(start, finish)) == expected
