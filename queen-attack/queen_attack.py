__author__ = 'dias'


def board(white, black):
    check_valid([white, black])

    if white == black:
        raise ValueError()

    # Everything looks ok. Proceed to build the board:
    brd =list()
    for x in range(8):
        row = ''
        for y in range(8):
            if (x, y) == white:
                square = 'W'
            elif (x, y) == black:
                square = 'B'
            else:
                square = '_'
            row += square
        brd.append(row)
    return brd

def can_attack(white_position, black_position):
    check_valid([white_position, black_position])

    if white_position == black_position:
        raise ValueError()

    white_x, white_y = white_position
    black_x, black_y = black_position

    # If they are on same horizontal or vertical line
    if white_x == black_x or white_y == black_y:
        return True

    # if they are on diagnol.
    if abs(float(white_y - black_y)/(white_x - black_x)) == 1.0:
        return True

    return False


def check_valid(positions):
    for position in positions:
        if len(position) != 2:
            raise ValueError()
        if not (0 <= position[0] <= 7 and 0 <= position[1] <= 7):
            raise ValueError()

print(can_attack((4, 2), (0, 5)))
