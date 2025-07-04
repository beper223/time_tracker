class CustomBaseException(Exception):

    def __init__(self, message: str, code: str = None):
        self.message = message
        self.code = code or self.__class__.__name__
        super().__init__(self.message)

class EntityNotFoundException(CustomBaseException):
    pass


class DatabaseException(CustomBaseException):
    pass
