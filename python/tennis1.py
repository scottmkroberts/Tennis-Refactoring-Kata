class TennisGame1:
    """Tracks points for a single tennis game and renders the current score."""

    POINT_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
    ALL_SUFFIX = "-All"
    DEUCE = "Deuce"
    ADVANTAGE_PREFIX = "Advantage "
    WIN_PREFIX = "Win for "

    def __init__(self, player1_name, player2_name):
        """Store the player names and start both players at zero points."""
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
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

    def score(self):
        """Return the current score as a tennis score string.

        Three cases, checked in order:
        1. Equal points: "Love-All" / "Fifteen-All" / "Thirty-All" for 0-2,
           otherwise "Deuce" (3-3, 4-4, 5-5, ...).
        2. Either player at >=4 points (and scores unequal): "Advantage" if
           the point difference is 1, otherwise "Win for" whoever is ahead.
        3. Otherwise (both under 4, unequal): "<p1 score>-<p2 score>" built
           from POINT_NAMES, indexed 0-3.

        Note: the "Advantage"/"Win for" strings hardcode the literal names
        "player1"/"player2" rather than self.player1_name/self.player2_name,
        so this only reads correctly when those are the names in use.
        """
        result = ""
        temp_score = 0
        if self.p1points == self.p2points:
            result = (
                self.POINT_NAMES[self.p1points] + self.ALL_SUFFIX
                if self.p1points < 3
                else self.DEUCE
            )
        elif self.p1points >= 4 or self.p2points >= 4:
            minus_result = self.p1points - self.p2points
            if minus_result == 1:
                result = self.ADVANTAGE_PREFIX + "player1"
            elif minus_result == -1:
                result = self.ADVANTAGE_PREFIX + "player2"
            elif minus_result >= 2:
                result = self.WIN_PREFIX + "player1"
            else:
                result = self.WIN_PREFIX + "player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.p1points
                else:
                    result += "-"
                    temp_score = self.p2points
                result += self.POINT_NAMES[temp_score]
        return result
