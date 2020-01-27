from abc import ABCMeta, abstractmethod


class BaseTask(metaclass=ABCMeta):
    hours = '*'
    minutes = '*'
    seconds = '*'

    @abstractmethod
    def run(self):
        pass
