__author__ = 'DIA'


def animation(speed, init_position):
    frames = list()

    def collect_frames(position):
        frames.append(format_position(position))
        if is_exit_condition(position):
            return frames

        total_length = len(position)
        new_position = list(position)
        for idx, x in enumerate(position):
            if not ignore(x, idx, speed, total_length):
                move_particle(x, idx, speed, new_position)
            ## This is where particle is bumbed out of container.
            elif x == 'R' and idx + speed >= total_length or x == 'L' and idx - speed < 0:
                new_position.pop(idx)
                new_position.insert(idx, '.')

        return collect_frames(''.join(new_position))

    return collect_frames(init_position)


## Removing the Current Char from the index and replacing it with '.'
## Next is to move to particle to new index and replace that as well.
def move_particle(ch, idx, speed, new_position):
    new_position.pop(idx)
    new_position.insert(idx, '.')
    new_idx = (idx + speed) if ch == 'R' else (idx - speed)
    new_position.pop(new_idx)
    new_position.insert(new_idx, ch)


def ignore(ch, idx, speed, total_length):
    if ch == '.':
        return True
    if ch == 'R' and idx + speed >= total_length:
        return True
    if ch == 'L' and idx - speed < 0:
        return True
    return False


def is_exit_condition(position):
    for c in position:
        if c != '.':
            return False
    return True


def format_position(position):
    return ''.join(['X' if ch != '.' else ch for ch in position])


frames = animation(2, init_position='LRRL.LR.LRR.R.LRRL.')
for frame in frames:
    print(frame)