class NotFoundError(Exception):
    def __init__(self, message) -> None:
        if message:
            self.message = message
        else:
            self.message = None
        
    def __str__(self) -> str:
        if self.message:
            return '{0} '.format(self.message)
        else:
            return 'NotfoundError has been raised'

class AlreadyExistsError(Exception):
    def __init__(self, message) -> None:
        if message:
            self.message = message
        else:
            self.message = None
        
    def __str__(self) -> str:
        if self.message:
            return '{0} '.format(self.message)
        else:
            return 'AlreadyExistsError has been raised'