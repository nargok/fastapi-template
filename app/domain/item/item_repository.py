from abc import ABC, abstractmethod


class ItemRepository(ABC):
    @abstractmethod
    def save():
        raise NotImplementedError

    @abstractmethod
    def find():
        raise NotImplementedError
