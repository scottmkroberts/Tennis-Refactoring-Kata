class TennisGame1:
    """Tracks points for a single tennis game and renders the current score."""

    POINT_NAMES: list[str] = ["Love", "Fifteen", "Thirty", "Forty"]
    DEUCE: str = "Deuce"

    def __init__(
        self, player1_name: str, player2_name: str, tiebreak: bool = False
    ) -> None:
        """Store the player names and start both players at zero points."""
        self.player1_name: str = player1_name
        self.player2_name: str = player2_name
        self.p1points: int = 0
        self.p2points: int = 0
        self.tiebreak: bool = tiebreak

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

        Dispatches on self.tiebreak: a tiebreak game reports raw point
        counts ("6-5", "0-All") and is won at 7+ points with a 2+ point
        lead; a regular game reports the usual tennis terms (Love/
        Fifteen/Thirty/Forty, Deuce, Advantage, Win for).
        """
        leader_name: str = self._leader_name()

        if self.tiebreak:
            if self._is_tied():
                return f"{self.p1points}-All"
            if self._is_tiebreak_won():
                return f"Win for {leader_name}"
            return f"{self.p1points}-{self.p2points}"

        else:
            if self._is_tied():
                return self._tied_score()
            if self._is_endgame():
                return self._endgame_score(leader_name)
            return self._regular_score()

    def _is_tied(self) -> bool:
        return self.p1points == self.p2points

    def _is_endgame(self) -> bool:
        return self.p1points >= 4 or self.p2points >= 4

    def _is_tiebreak_won(self) -> bool:
        point_difference: int = abs(self.p1points - self.p2points)
        return max(self.p1points, self.p2points) >= 7 and point_difference >= 2

    def _tied_score(self) -> str:
        """ "Love-All" / "Fifteen-All" / "Thirty-All" for 0-2, else "Deuce"."""
        return (
            f"{self.POINT_NAMES[self.p1points]}-All"
            if self.p1points < 3
            else self.DEUCE
        )

    def _leader_name(self) -> str:
        """Return the name of whichever player currently has more points."""
        return self.player1_name if self.p1points > self.p2points else self.player2_name

    def _endgame_score(self, leader_name: str) -> str:
        """ "Advantage" at a 1-point lead, "Win for" at a 2+ point lead."""
        point_difference: int = abs(self.p1points - self.p2points)
        return (
            f"Advantage {leader_name}"
            if point_difference == 1
            else f"Win for {leader_name}"
        )

    def _regular_score(self) -> str:
        """ "<p1 score>-<p2 score>", e.g. "Forty-Fifteen"."""
        return f"{self.POINT_NAMES[self.p1points]}-{self.POINT_NAMES[self.p2points]}"
