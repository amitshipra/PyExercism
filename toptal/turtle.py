DIRECTIONS_ORDER = ['North', 'East', 'South', 'West']


def solution(A):
    if len(A) == 0:
        return 0
    position = (0, 0, 0, '')
    moves = list()
    for move_idx, advance in enumerate(A):
        direction = next_direction(move_idx)
        if direction is 'North':
            x, y, steps = position[0], position[1] + advance, advance
        elif direction is 'South':
            x, y, steps = position[0], position[1] - advance, advance
        elif direction is 'East':
            x, y, steps = position[0] + advance, position[1], advance
        elif direction is 'West':
            x, y, steps = position[0] - advance, position[1], advance
        position = x, y, 0
        moves.append((x, y, steps))
    return moves


def find_intersection(moves):
    # Find lines between lines for each point pair and check to see if they intersect.
    # Couldn't find the suitable algo.
    return 0


def next_direction(move_index):
    idx = move_index % 4
    return DIRECTIONS_ORDER[idx]


print(solution([1, 3, 2, 5, 4, 4, 6, 3, 2]))
