class TennisGame2:
    """Tracks points for a single tennis game and renders the current score.

    This is the deliberately messy/unrefactored version of the kata: score()
    rebuilds the result through a long run of non-exclusive `if` blocks
    (not `elif`), relying on later blocks to overwrite earlier ones for the
    same score, and p1res/p2res are shared scratch variables reused (without
    being reset) across several of those blocks.
    """

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
            self.p1_score()
        else:
            self.p2_score()

    def score(self):
        """Return the current score as a tennis score string.

        Walks every score range (tied, one player at love, both 1-3 and
        unequal, advantage, win) as its own `if` block and overwrites
        `result` each time a later block's condition also matches, rather
        than branching once. The "Advantage"/"Win for" strings hardcode the
        literal names "player1"/"player2" instead of
        self.player1_name/self.player2_name, so output is only correct when
        those are the names in use.
        """
        result = ""
        if self.p1points == self.p2points and self.p1points < 3:
            if self.p1points == 0:
                result = "Love"
            if self.p1points == 1:
                result = "Fifteen"
            if self.p1points == 2:
                result = "Thirty"
            result += "-All"
        if self.p1points == self.p2points and self.p1points > 2:
            result = "Deuce"

        p1res = ""
        p2res = ""
        if self.p1points > 0 and self.p2points == 0:
            if self.p1points == 1:
                p1res = "Fifteen"
            if self.p1points == 2:
                p1res = "Thirty"
            if self.p1points == 3:
                p1res = "Forty"

            p2res = "Love"
            result = p1res + "-" + p2res
        if self.p2points > 0 and self.p1points == 0:
            if self.p2points == 1:
                p2res = "Fifteen"
            if self.p2points == 2:
                p2res = "Thirty"
            if self.p2points == 3:
                p2res = "Forty"

            p1res = "Love"
            result = p1res + "-" + p2res

        if self.p1points > self.p2points and self.p1points < 4:
            if self.p1points == 2:
                p1res = "Thirty"
            if self.p1points == 3:
                p1res = "Forty"
            if self.p2points == 1:
                p2res = "Fifteen"
            if self.p2points == 2:
                p2res = "Thirty"
            result = p1res + "-" + p2res
        if self.p2points > self.p1points and self.p2points < 4:
            if self.p2points == 2:
                p2res = "Thirty"
            if self.p2points == 3:
                p2res = "Forty"
            if self.p1points == 1:
                p1res = "Fifteen"
            if self.p1points == 2:
                p1res = "Thirty"
            result = p1res + "-" + p2res

        if self.p1points > self.p2points and self.p2points >= 3:
            result = "Advantage player1"

        if self.p2points > self.p1points and self.p1points >= 3:
            result = "Advantage player2"

        if (
            self.p1points >= 4
            and self.p2points >= 0
            and (self.p1points - self.p2points) >= 2
        ):
            result = "Win for player1"
        if (
            self.p2points >= 4
            and self.p1points >= 0
            and (self.p2points - self.p1points) >= 2
        ):
            result = "Win for player2"
        return result

    def set_p1_score(self, number):
        """Award player1 `number` points. Not used by the current test suite."""
        for i in range(number):
            self.p1_score()

    def set_p2_score(self, number):
        """Award player2 `number` points. Not used by the current test suite."""
        for i in range(number):
            self.p2_score()

    def p1_score(self):
        """Award player1 a single point."""
        self.p1points += 1

    def p2_score(self):
        """Award player2 a single point."""
        self.p2points += 1
