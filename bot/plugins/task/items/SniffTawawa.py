import time

from bot.plugins.task.items.BaseTask import BaseTask


class SniffTawawa(BaseTask):

    def __init__(self):
        pass

    def run(self):
        if self.run_check():
            pass

    @staticmethod
    def run_check():
        week = int(time.strftime('%w', time.localtime()))
        hour = int(time.strftime('%H', time.localtime()))
        min = int(time.strftime('%M', time.localtime()))

        if week == 1 and 9 < hour < 12 and min % 5 == 0:
            return True

        return False
