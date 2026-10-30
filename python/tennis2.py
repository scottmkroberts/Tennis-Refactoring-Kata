class TennisGame2:
    """Tracks points for a single tennis game and renders the current score.

    score() dispatches on four named conditions - tied, regular (both under
    4), win, and advantage.
    """

    POINT_NAMES: list[str] = ["Love", "Fifteen", "Thirty", "Forty"]

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
            self.p1_score()
        else:
            self.p2_score()

    def score(self) -> str:
        """Return the current score as a tennis score string."""
        if self._is_tied():
            return self._tied_score()
        if self._is_regular():
            return self._regular_score()
        if self._is_win():
            return self._win_score()
        if self._is_advantage():
            return self._advantage_score()
        return ""

    def set_p1_score(self, number: int) -> None:
        """Add `number` points to player1's existing score."""
        self.p1points += number

    def set_p2_score(self, number: int) -> None:
        """Add `number` points to player2's existing score."""
        self.p2points += number

    def p1_score(self) -> None:
        """Award player1 a single point."""
        self.p1points += 1

    def p2_score(self) -> None:
        """Award player2 a single point."""
        self.p2points += 1

    def _is_tied(self) -> bool:
        return self.p1points == self.p2points

    def _is_regular(self) -> bool:
        """Both players are under 4 points (and, by dispatch order, unequal)."""
        return self.p1points < 4 and self.p2points < 4

    def _is_advantage(self) -> bool:
        """True whenever one player leads with >=3 points; only correct
        once _is_win() has already been ruled out, since a player leading
        by 2+ (a win) also satisfies this condition."""
        return (self.p1points > self.p2points and self.p2points >= 3) or (
            self.p2points > self.p1points and self.p1points >= 3
        )

    def _is_win(self) -> bool:
        """True whenever one player leads by 2 or more points."""
        return (self.p1points >= 4 and (self.p1points - self.p2points) >= 2) or (
            self.p2points >= 4 and (self.p2points - self.p1points) >= 2
        )

    def _tied_score(self) -> str:
        """ "Love-All" / "Fifteen-All" / "Thirty-All" for 0-2, else "Deuce"."""
        if self.p1points > 2:
            return "Deuce"
        return f"{self.POINT_NAMES[self.p1points]}-All"

    def _regular_score(self) -> str:
        """ "<p1 score>-<p2 score>", e.g. "Forty-Fifteen"."""
        return f"{self.POINT_NAMES[self.p1points]}-{self.POINT_NAMES[self.p2points]}"

    def _advantage_score(self) -> str:
        """Hardcodes the literal names "player1"/"player2" rather than
        self.player1_name/self.player2_name, so output is only correct
        when those are the names in use."""
        if self.p1points > self.p2points:
            return "Advantage player1"
        return "Advantage player2"

    def _win_score(self) -> str:
        """Hardcodes the literal names "player1"/"player2" rather than
        self.player1_name/self.player2_name, so output is only correct
        when those are the names in use."""
        if self.p1points > self.p2points:
            return "Win for player1"
        return "Win for player2"
