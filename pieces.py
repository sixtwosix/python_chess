## Chess piece class
class Piece:
    def __init__(self, team, type, image, killable=False):
        self.team = team
        self.type = type
        self.killable = killable
        self.image = image

class Empty_Sqr:
    def __init__(self, team=None, killable=False):
        self.team = team
        self.killable = killable