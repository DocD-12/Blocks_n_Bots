class field_object():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, orientation):
        if orientation == 0:
            self.x += -1
        elif orientation == 1:
            self.y += 1
        elif orientation == 2:
            self.x += 1
        elif orientation == 3:
            self.y += -1

    def get_coord(self):
        return self.x, self.y


class player(field_object):

    def __init__(self, x, y, team):
        field_object.__init__(self, x, y)
        self.team = team
        self.coin = 0

    def get_team(self):
        return self.team

    def __str__(self):
        if self.team == 'blue':
            return 'B'
        elif self.team == 'red':
            return 'R'
        else:
            return 'P'

    def get_coin(self):
        return self.coin

    def grab_coin(self):
        self.coin = 1

    def del_coin(self):
        self.coin = 0


class block(field_object):

    def __init__(self, x, y, enable_move=False):
        field_object.__init__(self, x, y)
        self.enable_move = enable_move

    def __str__(self):
        if self.enable_move is False: return 'X'
        return 'x'

    def get_enable_move(self):
        return self.enable_move
