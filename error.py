from abc import  abstractmethod


class Error:
    def __init__(self):
        self.error = False
    @abstractmethod
    def ERROR(self, statement: str) -> None:
        pass
