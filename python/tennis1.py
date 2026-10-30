class TennisGame1:
    """Tracks points for a single tennis game and renders the current score."""

    POINT_NAMES: list[str] = ["Love", "Fifteen", "Thirty", "Forty"]
    ALL_SUFFIX: str = "-All"
    DEUCE: str = "Deuce"
    ADVANTAGE_PREFIX: str = "Advantage "
    WIN_PREFIX: str = "Win for "

    def __init__(self, player1_name: str, player2_name: str) -> None:
        """Store the player names and start both players at zero points."""
        self.player1_name: str = player1_name
        self.player2_name: str = player2_name
        self.p1points: int = 0
        self.p2points: int = 0

    def _is_tied(self) -> bool:
        return self.p1points == self.p2points

    def _is_endgame(self) -> bool:
        return self.p1points >= 4 or self.p2points >= 4

    def won_point(self, player_name: str) -> None:
        """Award a point to the named player.

        Raises ValueError if player_name is neither player1_name nor
        player2_name.
        """
        if player_name == self.player1_name:
            self.p1points += 1
        elif player_name == self.player2_name:
            self.p2points += 1
        else:
            raise ValueError(f"Unknown player name: {player_name!r}")

    def score(self) -> str:
        """Return the current score as a tennis score string.

        Three cases, checked in order:
        1. Equal points: "Love-All" / "Fifteen-All" / "Thirty-All" for 0-2,
           otherwise "Deuce" (3-3, 4-4, 5-5, ...).
        2. Either player at >=4 points (and scores unequal): "Advantage" if
           the point difference is 1, otherwise "Win for" whoever is ahead.
        3. Otherwise (both under 4, unequal): "<p1 score>-<p2 score>" built
           from POINT_NAMES, indexed 0-3.
        """
        result: str = ""
        temp_score: int = 0
        if self._is_tied():
            result = (
                self.POINT_NAMES[self.p1points] + self.ALL_SUFFIX
                if self.p1points < 3
                else self.DEUCE
            )
        elif self._is_endgame():
            minus_result: int = self.p1points - self.p2points
            if minus_result == 1:
                result = self.ADVANTAGE_PREFIX + self.player1_name
            elif minus_result == -1:
                result = self.ADVANTAGE_PREFIX + self.player2_name
            elif minus_result >= 2:
                result = self.WIN_PREFIX + self.player1_name
            else:
                result = self.WIN_PREFIX + self.player2_name
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.p1points
                else:
                    result += "-"
                    temp_score = self.p2points
                result += self.POINT_NAMES[temp_score]
        return result
