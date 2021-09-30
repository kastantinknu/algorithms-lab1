from LDFS.answer import Answer
import copy


class LDFS:

    def __init__(self, initial_chessboard, limit):
        self.initial_chessboard = initial_chessboard
        self.limit = limit
        self.answer = None
        self.__checked_states = []
        self.iterations = 0
        self.states_number = 0
        self.dead_ends = 0

    def __recursive_DLS(self, current_state, current_depth):
        self.iterations += 1
        cutoff_occurred = False
        if LDFS.__chessboard_validation(current_state):
            return Answer(True, result_chessboard=current_state)
        if current_depth == self.limit:

            return Answer(False, error_message='cutoff')

        successors = self.__get_successors(current_state)
        self.states_number += len(successors)
        for successor in successors:
            result = self.__recursive_DLS(successor, current_depth + 1)
            if not result.is_success:
                cutoff_occurred = True if result.error_message == 'cutoff' else False
            if result.is_success:
                return result
        if cutoff_occurred:
            return Answer(False, error_message='cutoff')
        else:
            return Answer(False, error_message='failure')

    def depth_limited_search(self):
        self.__checked_states = []
        self.answer = self.__recursive_DLS(self.initial_chessboard, 0)
        self.__checked_states = []

    @staticmethod
    def __chessboard_validation(chessboard):
        for i in range(8):
            for j in range(i + 1, 8):
                if chessboard[i][0] == chessboard[j][0] or chessboard[i][1] == chessboard[j][1] \
                        or abs(chessboard[i][0] - chessboard[j][0]) == abs(chessboard[i][1] - chessboard[j][1]):
                    return False
        return True

    def __get_successors(self, chessboard):
        result = []
        for i in range(8):
            for j in range(8):
                temp = copy.deepcopy(chessboard)
                temp[i][0] = j
                if not chessboard[i][0] == j and temp not in self.__checked_states:
                    result.append(copy.deepcopy(temp))
                    self.__checked_states.append(temp)
        if len(result) == 0:
            self.dead_ends += 1
        return result
