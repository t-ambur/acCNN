import keyInjector as KI
import time

KEYPRESS_DELAY = KI.NO_DELAY


class Control:
    def __init__(self, ahk):
        self.ahk = ahk
        self.print = False

    @staticmethod
    def buy_1():
        KI.KeyPress(KI.KEY1, KEYPRESS_DELAY)
        time.sleep(1)
        KI.KeyPress(KI.SPACE_BAR, KEYPRESS_DELAY)
        time.sleep(1)

    @staticmethod
    def grab_item_1():
        KI.KeyPress(KI.J_KEY, KEYPRESS_DELAY)
        time.sleep(1)
