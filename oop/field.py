from field_object import *


class field():

    def __init__(self, size):
        self.size = size
        self.objects = []

    def add_object(self, object):
        self.objects.append(object)
        return len(self.objects) - 1

    def del_object(self, object):
        self.objects.pop(object)

    def print_field(self):
        field = [['0' for _ in range(self.size)] for _ in range(self.size)]

        for object in self.objects:
            x, y = object.get_coord()
            field[x][y] = str(object)

        for i in field:
            print(' '.join(i))

    def move_object(self, index, orient):
        self.objects[index].move(orient)