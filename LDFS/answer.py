class Answer:
    def __init__(self, is_success, error_message=None, result_chessboard=None):
        self.is_success = is_success
        self.error_message = error_message
        self.result_chessboard = result_chessboard

    def __str__(self):
        return ('is success: ' + str(self.is_success) + '\n'
                + 'result chessboard: ' + str(self.result_chessboard) + '\n'
                + 'error_message: ' + str(self.error_message))
