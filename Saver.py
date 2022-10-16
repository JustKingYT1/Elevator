import json as j
from abc import ABC, abstractmethod


class Saver(ABC):
    @staticmethod
    @abstractmethod
    def save(file: str, parameters):
        pass


class SaverToJSON(Saver):
    @staticmethod
    def save(file, parameters):
        with open(file, "w") as write_file:
            return j.dump(parameters, write_file)
