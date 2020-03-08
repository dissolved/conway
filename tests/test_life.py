from conway.life import Life, neighbor_rules
import pytest


def test_empty_cell():
    assert neighbor_rules(alive=False, neighbors=0) is False
    assert neighbor_rules(alive=False, neighbors=1) is False
    assert neighbor_rules(alive=False, neighbors=2) is False
    assert neighbor_rules(alive=False, neighbors=3) is True
    assert neighbor_rules(alive=False, neighbors=4) is False
    assert neighbor_rules(alive=False, neighbors=5) is False
    assert neighbor_rules(alive=False, neighbors=6) is False
    assert neighbor_rules(alive=False, neighbors=7) is False
    assert neighbor_rules(alive=False, neighbors=8) is False


def test_populated_cell():
    assert neighbor_rules(alive=True, neighbors=0) is False
    assert neighbor_rules(alive=True, neighbors=1) is False
    assert neighbor_rules(alive=True, neighbors=2) is True
    assert neighbor_rules(alive=True, neighbors=3) is True
    assert neighbor_rules(alive=True, neighbors=4) is False
    assert neighbor_rules(alive=True, neighbors=5) is False
    assert neighbor_rules(alive=True, neighbors=6) is False
    assert neighbor_rules(alive=True, neighbors=7) is False
    assert neighbor_rules(alive=True, neighbors=8) is False


@pytest.fixture
def game():
    return Life()


@pytest.fixture
def loaded_game():
    game = Life()
    game.load('tests/game1.txt')
    return game


def test_randomize_defaults(game):
    game.randomize()
    assert game.population == 500
    assert game.size_x == 40
    assert game.size_y == 40


def test_randomize(game):
    game.randomize(size_x=10, size_y=20, population=33)
    assert game.population == 33
    assert game.size_x == 10
    assert game.size_y == 20


def test_load(loaded_game):
    assert loaded_game.population == 10
    assert loaded_game.size_x == 40
    assert loaded_game.size_y == 10


def test_equality(game, loaded_game):
    game.load('tests/game1.txt')
    assert loaded_game == game


def test_iterate(game, loaded_game):
    game.load('tests/game2.txt')
    loaded_game.iterate()
    assert loaded_game == game
    game.load('tests/game3.txt')
    loaded_game.iterate()
    assert loaded_game == game
    game.load('tests/game4.txt')
    loaded_game.iterate()
    assert loaded_game == game
    game.load('tests/game5.txt')
    loaded_game.iterate()
    assert loaded_game == game
    game.load('tests/game6.txt')
    loaded_game.iterate()
    assert loaded_game == game
