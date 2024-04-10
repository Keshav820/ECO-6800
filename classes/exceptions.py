class BadAuthException(Exception):
    def __init__(self, message="Invalid or expired token"):
        self.message = message
        super().__init__(self.message)