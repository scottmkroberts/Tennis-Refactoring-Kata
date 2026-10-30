class TennisGame3:
    """Tracks points for a single tennis game and renders the current score."""

    def __init__(self, player1_name: str, player2_name: str) -> None:
        """Store the player names and start both players at zero points."""
        self.p1_n: str = player1_name
        self.p2_n: str = player2_name
        self.p1: int = 0
        self.p2: int = 0

    def won_point(self, n: str) -> None:
        """Award a point to the named player.

        Anything other than the exact string "player1" is treated as a
        point for player2 - n is otherwise unused and unvalidated.
        """
        if n == "player1":
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self) -> str:
        """Return the current score as a tennis score string.

        The first branch covers every combination where both players are
        under 4 points except a 3-3 tie - `self.p1 + self.p2 < 6` excludes
        it, so 3-3 falls through to the second branch's "Deuce" instead of
        being treated as "Forty-All". The second branch covers ties of 3
        or more ("Deuce") and endgame states, where the point difference
        decides "Advantage" (1) from "Win for" (2+) for whoever is ahead.
        """
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p: list[str] = ["Love", "Fifteen", "Thirty", "Forty"]
            s: str = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if self.p1 == self.p2:
                return "Deuce"
            s: str = self.p1_n if self.p1 > self.p2 else self.p2_n
            return (
                "Advantage " + s
                if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1)
                else "Win for " + s
            )
