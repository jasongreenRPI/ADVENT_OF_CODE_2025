def loadFile(filename):
    lis = []
    with open(filename, 'r') as f:
        for line in f:
            lis.append(line.strip())
    return lis


def count_zero_crossings(starting, direction, totalMoves):
    if direction == 'R':
        first = (100 - starting) % 100
    else:  # 'L'
        first = starting % 100

    if first == 0:
        first = 100

    if first > totalMoves:
        return 0

    return 1 + (totalMoves - first) // 100


def main():
    moves = loadFile('./aoc_day1/day1_input.txt')

    starting = 50
    crosses_zero = 0

    for move in moves:
        direction = move[0]
        totalMoves = int(move[1:])

        crosses_zero += count_zero_crossings(starting, direction, totalMoves)

        if direction == 'R':
            starting = (starting + totalMoves) % 100
        elif direction == 'L':
            starting = (starting - totalMoves) % 100
        else:
            raise ValueError("LOLOL")

    return crosses_zero


if __name__ == "__main__":
    res = main()
    print(res)
