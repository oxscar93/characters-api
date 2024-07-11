from http import HTTPStatus


class NotFoundException(Exception):
    def __init__(self, message: str = None, status_code: int = 400):
        super(NotFoundException, self).__init__(message)
        self._message = message
        self._status_code = status_code

    @property
    def error_message(self):
        if self._message is None:
            return "Entity not found"

        return self._message

    @property
    def status_code(self):
        return HTTPStatus.BAD_REQUEST
    

class EntityAlreadyExists(Exception):
    def __init__(self, message: str = None, status_code: int = 400):
        super(EntityAlreadyExists, self).__init__(message)
        self._message = message
        self._status_code = status_code

    @property
    def error_message(self):
        if self._message is None:
            return "Entity already exists in database"

        return self._message

    @property
    def status_code(self):
        return HTTPStatus.BAD_REQUEST