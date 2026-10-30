import pytest

from tennis1 import TennisGame1
from tennis2 import TennisGame2
from tennis3 import TennisGame3
from tennis4 import TennisGame4
from tennis5 import TennisGame5
from tennis6 import TennisGame6
from tennis7 import TennisGame7

test_cases = [
    pytest.param(0, 0, "Love-All", "player1", "player2", id="start of game"),
    pytest.param(1, 1, "Fifteen-All", "player1", "player2", id="fifteen all"),
    pytest.param(2, 2, "Thirty-All", "player1", "player2", id="thirty all"),
    pytest.param(3, 3, "Deuce", "player1", "player2", id="deuce at forty all"),
    pytest.param(4, 4, "Deuce", "player1", "player2", id="deuce after advantage"),
    pytest.param(
        1, 0, "Fifteen-Love", "player1", "player2", id="p1 leads fifteen-love"
    ),
    pytest.param(
        0, 1, "Love-Fifteen", "player1", "player2", id="p2 leads fifteen-love"
    ),
    pytest.param(2, 0, "Thirty-Love", "player1", "player2", id="p1 leads thirty-love"),
    pytest.param(0, 2, "Love-Thirty", "player1", "player2", id="p2 leads thirty-love"),
    pytest.param(3, 0, "Forty-Love", "player1", "player2", id="p1 leads forty-love"),
    pytest.param(0, 3, "Love-Forty", "player1", "player2", id="p2 leads forty-love"),
    pytest.param(4, 0, "Win for player1", "player1", "player2", id="p1 wins from love"),
    pytest.param(0, 4, "Win for player2", "player1", "player2", id="p2 wins from love"),
    pytest.param(
        2, 1, "Thirty-Fifteen", "player1", "player2", id="p1 leads thirty-fifteen"
    ),
    pytest.param(
        1, 2, "Fifteen-Thirty", "player1", "player2", id="p2 leads thirty-fifteen"
    ),
    pytest.param(
        3, 1, "Forty-Fifteen", "player1", "player2", id="p1 leads forty-fifteen"
    ),
    pytest.param(
        1, 3, "Fifteen-Forty", "player1", "player2", id="p2 leads forty-fifteen"
    ),
    pytest.param(
        4, 1, "Win for player1", "player1", "player2", id="p1 wins from fifteen"
    ),
    pytest.param(
        1, 4, "Win for player2", "player1", "player2", id="p2 wins from fifteen"
    ),
    pytest.param(
        3, 2, "Forty-Thirty", "player1", "player2", id="p1 leads forty-thirty"
    ),
    pytest.param(
        2, 3, "Thirty-Forty", "player1", "player2", id="p2 leads forty-thirty"
    ),
    pytest.param(
        4, 2, "Win for player1", "player1", "player2", id="p1 wins from thirty"
    ),
    pytest.param(
        2, 4, "Win for player2", "player1", "player2", id="p2 wins from thirty"
    ),
    pytest.param(4, 3, "Advantage player1", "player1", "player2", id="p1 advantage"),
    pytest.param(3, 4, "Advantage player2", "player1", "player2", id="p2 advantage"),
    pytest.param(
        5, 4, "Advantage player1", "player1", "player2", id="p1 advantage after deuce"
    ),
    pytest.param(
        4, 5, "Advantage player2", "player1", "player2", id="p2 advantage after deuce"
    ),
    pytest.param(
        15,
        14,
        "Advantage player1",
        "player1",
        "player2",
        id="p1 advantage in long game",
    ),
    pytest.param(
        14,
        15,
        "Advantage player2",
        "player1",
        "player2",
        id="p2 advantage in long game",
    ),
    pytest.param(
        6, 4, "Win for player1", "player1", "player2", id="p1 wins after deuce"
    ),
    pytest.param(
        4, 6, "Win for player2", "player1", "player2", id="p2 wins after deuce"
    ),
    pytest.param(
        16, 14, "Win for player1", "player1", "player2", id="p1 wins long game"
    ),
    pytest.param(
        14, 16, "Win for player2", "player1", "player2", id="p2 wins long game"
    ),
]


def play_points(game, p1_points, p2_points, p1_name, p2_name):
    for i in range(max(p1_points, p2_points)):
        if i < p1_points:
            game.won_point(p1_name)
        if i < p2_points:
            game.won_point(p2_name)
    return game


def play_game(TennisGame, p1_points, p2_points, p1_name, p2_name):
    game = TennisGame(p1_name, p2_name)
    return play_points(game, p1_points, p2_points, p1_name, p2_name)


def play_game_with_tiebreaker(
    TennisGame, p1_points, p2_points, p1_name, p2_name, tiebreak=True
):
    game = TennisGame(p1_name, p2_name, tiebreak)
    return play_points(game, p1_points, p2_points, p1_name, p2_name)


@pytest.mark.parametrize(
    "TennisGameClass",
    [
        TennisGame1,
        TennisGame2,
        TennisGame3,
        TennisGame4,
        TennisGame5,
        TennisGame6,
    ],
)
@pytest.mark.parametrize(
    "p1_points p2_points score p1_name p2_name".split(), test_cases
)
def test_get_score_most_games(
    TennisGameClass, p1_points, p2_points, score, p1_name, p2_name
):
    game = play_game(TennisGameClass, p1_points, p2_points, p1_name, p2_name)
    assert score == game.score()


@pytest.mark.parametrize(
    "p1_points p2_points score p1_name p2_name".split(), test_cases
)
def test_get_score_game7(p1_points, p2_points, score, p1_name, p2_name):
    game = play_game(TennisGame7, p1_points, p2_points, p1_name, p2_name)
    assert "Current score: " + score + ", enjoy your game!" == game.score()


def test_won_point_with_unrecognized_name_raises():
    game = TennisGame1("player1", "player2")
    with pytest.raises(ValueError):
        game.won_point("not-a-real-player")


@pytest.mark.parametrize(
    "p1_points p2_points score".split(),
    [
        (4, 3, "Advantage Venus"),
        (3, 4, "Advantage Serena"),
        (4, 0, "Win for Venus"),
        (0, 4, "Win for Serena"),
    ],
)
def test_score_uses_actual_player_names(p1_points, p2_points, score):
    game = play_game(TennisGame1, p1_points, p2_points, "Venus", "Serena")
    assert score == game.score()


@pytest.mark.parametrize(
    "p1_points, p2_points, expected_score",
    [
        pytest.param(0, 6, "0-All", id="tiebreak start"),
        pytest.param(7, 6, "7-6", id="one clear is not a win"),
    ],
)
def test_tiebreak_score(p1_points, p2_points, expected_score):
    game = play_game_with_tiebreaker(
        TennisGame1, p1_points, p2_points, "player1", "player2"
    )
    assert expected_score == game.score()
