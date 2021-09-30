from LDFS.LDFS import LDFS
from RBFS.RBFS import RBFS
import random
import time


def generate_chessboards(number):
    result = []
    for _ in range(number):
        board = []
        for j in range(8):
            is_added = False
            while not is_added:
                queen = [random.randint(0, 7), j]
                if queen not in board:
                    board.append(queen)
                    is_added = True
        result.append(board)
    return result


chessboards = [
    [[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [3, 7]],
    [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]],
    [[1, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [3, 7]],
    [[3, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [3, 7]],
    [[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [5, 5], [1, 6], [3, 7]],
    [[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [9, 7]],
    [[4, 0], [0, 1], [7, 2], [3, 3], [2, 4], [6, 5], [1, 6], [3, 7]],
    [[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [2, 6], [3, 7]],
    [[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [0, 7]],
    [[4, 0], [0, 1], [0, 2], [5, 3], [2, 4], [6, 5], [1, 6], [3, 7]],
    [[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [6, 7]],
    [[4, 0], [0, 1], [7, 2], [5, 3], [0, 4], [6, 5], [1, 6], [3, 7]],
    [[4, 0], [0, 1], [5, 2], [5, 3], [2, 4], [6, 5], [1, 6], [3, 7]],
    [[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [6, 6], [3, 7]],
    [[4, 0], [0, 1], [7, 2], [8, 3], [2, 4], [6, 5], [1, 6], [3, 7]],
    [[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [5, 7]],
    [[4, 0], [6, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [3, 7]],
    [[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [9, 5], [1, 6], [3, 7]],
    [[4, 0], [0, 1], [7, 2], [5, 3], [2, 4], [6, 5], [1, 6], [9, 7]],
    [[4, 0], [0, 1], [3, 2], [5, 3], [2, 4], [6, 5], [1, 6], [3, 7]]
]

print('------RBFS------')
for chessboard in generate_chessboards(20):
    start_time = time.time()
    rbfs = RBFS(chessboard)
    print('Input chessboard = ' + str(chessboard))
    rbfs.recursive_best_first_search()
    print(rbfs.answer)
    print('states number = ' + str(rbfs.states_number))
    print('iterations = ' + str(rbfs.iterations))
    print('dead ends = ' + str(rbfs.dead_ends))
    print("%s seconds" % (time.time() - start_time))
    print()

print('------LDFS------')
for chessboard in chessboards:
    start_time = time.time()
    ldfs = LDFS(chessboard, 10)
    print('Input chessboard = ' + str(chessboard))
    ldfs.depth_limited_search()
    print(ldfs.answer)
    print('states number = ' + str(ldfs.states_number))
    print('iterations = ' + str(ldfs.iterations))
    print('dead ends = ' + str(ldfs.dead_ends))
    print("%s seconds" % (time.time() - start_time))
    print()
