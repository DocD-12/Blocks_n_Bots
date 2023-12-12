from field import *
import os
from time import sleep


if __name__ == '__main__':
    size = 10
    os.system('cls')

    field = field(size)
    field.print_field()
    field.add_object(block(1, 1, True))

    for i in range(size):
        for j in range(size):
            if i == 0 or i == size-1:
                field.add_object(block(i, j))
            else:
                if j == 0 or j == size-1:
                    field.add_object(block(i, j))
                elif i == j: field.add_object(block(i, j, True))
    player1 = field.add_object(player(size-2, 1, 'blue'))
    player2 = field.add_object(player(1, size - 2, 'red'))

    while 1:
        sleep(1)
        os.system('cls')
        field.print_field()

        field.move_object(player1, 1)