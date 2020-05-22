import keyInjector as KI
import random

KEYPRESS_DELAY = .05


class Control:
    def __init__(self, ahk):
        self.ahk = ahk
        self.print = False

    @staticmethod
    def buy_1():
        KI.KeyPress(KI.KEY1, KEYPRESS_DELAY)
