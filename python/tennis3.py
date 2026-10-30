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

        Ties return immediately ("-All" under 3, else "Deuce"), so the
        remaining checks only ever see an unequal score. Then: both under
        4 is the regular "<p1 score>-<p2 score>" case, otherwise it's an
        endgame state, where the point difference decides "Advantage" (1)
        from "Win for" (2+) for whoever is ahead.
        """
        point_names: list[str] = ["Love", "Fifteen", "Thirty", "Forty"]
        if self._is_tied():
            return point_names[self.p1points] + "-All" if self.p1points < 3 else "Deuce"
        if self._is_regular():
            return point_names[self.p1points] + "-" + point_names[self.p2points]
        leader_name: str = (
            self.player1_name if self.p1points > self.p2points else self.player2_name
        )
        point_difference: int = self.p1points - self.p2points
        return (
            "Advantage " + leader_name
            if (point_difference * point_difference == 1)
            else "Win for " + leader_name
        )

    def _is_tied(self) -> bool:
        return self.p1points == self.p2points

    def _is_regular(self) -> bool:
        return self.p1points < 4 and self.p2points < 4
