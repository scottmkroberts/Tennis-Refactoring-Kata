class TennisGame3:
    """Tracks points for a single tennis game and renders the current score."""

    def __init__(self, player1_name: str, player2_name: str) -> None:
        """Store the player names and start both players at zero points."""
        self.player1_name: str = player1_name
        self.player2_name: str = player2_name
        self.p1points: int = 0
        self.p2points: int = 0

    def won_point(self, player_name: str) -> None:
        """Award a point to the named player.

        Anything other than the exact string "player1" is treated as a
        point for player2 - player_name is otherwise unused and unvalidated.
        """
        if player_name == "player1":
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self) -> str:
        """Return the current score as a tennis score string.

        The first branch covers every combination where both players are
        under 4 points except a 3-3 tie - `self.p1points + self.p2points < 6`
        excludes it, so 3-3 falls through to the second branch's "Deuce"
        instead of being treated as "Forty-All". The second branch covers
        ties of 3 or more ("Deuce") and endgame states, where the point
        difference decides "Advantage" (1) from "Win for" (2+) for whoever
        is ahead.
        """
        if (self.p1points < 4 and self.p2points < 4) and (
            self.p1points + self.p2points < 6
        ):
            point_names: list[str] = ["Love", "Fifteen", "Thirty", "Forty"]
            p1_score_name: str = point_names[self.p1points]
            return (
                p1_score_name + "-All"
                if (self.p1points == self.p2points)
                else p1_score_name + "-" + point_names[self.p2points]
            )
        else:
            if self.p1points == self.p2points:
                return "Deuce"
            leader_name: str = (
                self.player1_name
                if self.p1points > self.p2points
                else self.player2_name
            )
            point_difference: int = self.p1points - self.p2points
            return (
                "Advantage " + leader_name
                if (point_difference * point_difference == 1)
                else "Win for " + leader_name
            )
