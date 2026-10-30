class TennisGame1:
    """Tracks points for a single tennis game and renders the current score."""

    POINT_NAMES: list[str] = ["Love", "Fifteen", "Thirty", "Forty"]
    DEUCE: str = "Deuce"

    def __init__(self, player1_name: str, player2_name: str) -> None:
        """Store the player names and start both players at zero points."""
        self.player1_name: str = player1_name
        self.player2_name: str = player2_name
        self.p1points: int = 0
        self.p2points: int = 0

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
        """Return the current score as a tennis score string."""
        if self._is_tied():
            return self._tied_score()
        if self._is_endgame():
            return self._endgame_score()
        return self._regular_score()

    def _is_tied(self) -> bool:
        return self.p1points == self.p2points

    def _is_endgame(self) -> bool:
        return self.p1points >= 4 or self.p2points >= 4

    def _tied_score(self) -> str:
        """ "Love-All" / "Fifteen-All" / "Thirty-All" for 0-2, else "Deuce"."""
        return (
            f"{self.POINT_NAMES[self.p1points]}-All"
            if self.p1points < 3
            else self.DEUCE
        )

    def _endgame_score(self) -> str:
        """ "Advantage" at a 1-point lead, "Win for" at a 2+ point lead."""
        leader_name: str = (
            self.player1_name if self.p1points > self.p2points else self.player2_name
        )
        point_difference: int = abs(self.p1points - self.p2points)
        return (
            f"Advantage {leader_name}"
            if point_difference == 1
            else f"Win for {leader_name}"
        )

    def _regular_score(self) -> str:
        """ "<p1 score>-<p2 score>", e.g. "Forty-Fifteen"."""
        return f"{self.POINT_NAMES[self.p1points]}-{self.POINT_NAMES[self.p2points]}"
