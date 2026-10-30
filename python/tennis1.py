class TennisGame1:
    """Tracks points for a single tennis game and renders the current score."""

    def __init__(self, player1_name, player2_name):
        """Store the player names and start both players at zero points."""
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        """Award a point to the named player.

        Anything other than the exact string "player1" is treated as a
        point for player2 - player_name is otherwise unused and unvalidated.
        """
        if player_name == "player1":
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        """Return the current score as a tennis score string.

        Three cases, checked in order:
        1. Equal points: "Love-All" / "Fifteen-All" / "Thirty-All" for 0-2,
           otherwise "Deuce" (3-3, 4-4, 5-5, ...).
        2. Either player at >=4 points (and scores unequal): "Advantage" if
           the point difference is 1, otherwise "Win for" whoever is ahead.
        3. Otherwise (both under 4, unequal): "<p1 score>-<p2 score>" built
           from a lookup of 0-3 to "Love"/"Fifteen"/"Thirty"/"Forty".

        Note: the "Advantage"/"Win for" strings hardcode the literal names
        "player1"/"player2" rather than self.player1_name/self.player2_name,
        so this only reads correctly when those are the names in use.
        """
        result = ""
        temp_score = 0
        if self.p1points == self.p2points:
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")
        elif self.p1points >= 4 or self.p2points >= 4:
            minus_result = self.p1points - self.p2points
            if minus_result == 1:
                result = "Advantage player1"
            elif minus_result == -1:
                result = "Advantage player2"
            elif minus_result >= 2:
                result = "Win for player1"
            else:
                result = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.p1points
                else:
                    result += "-"
                    temp_score = self.p2points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result
