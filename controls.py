import keyInjector as KI
import time

KEYPRESS_DELAY = KI.NO_DELAY


class Control:
    def __init__(self, ahk):
        self.ahk = ahk
        self.print = False

    @staticmethod
    def buy(pos):
        if pos == 0:
            KI.KeyPress(KI.KEY1, KEYPRESS_DELAY)
        elif pos == 1:
            KI.KeyPress(KI.KEY2, KEYPRESS_DELAY)
        elif pos == 2:
            KI.KeyPress(KI.KEY3, KEYPRESS_DELAY)
        elif pos == 3:
            KI.KeyPress(KI.KEY4, KEYPRESS_DELAY)
        elif pos == 4:
            KI.KeyPress(KI.KEY5, KEYPRESS_DELAY)
        time.sleep(1)

    @staticmethod
    def toggle_store():
        KI.KeyPress(KI.SPACE_BAR, KEYPRESS_DELAY)
        time.sleep(1)

    @staticmethod
    def grab_item(pos):
        if pos == 1:
            KI.KeyPress(KI.J_KEY, KEYPRESS_DELAY)
        elif pos == 2:
            KI.KeyPress(KI.K_KEY, KEYPRESS_DELAY)
        elif pos == 3:
            KI.KeyPress(KI.L_KEY, KEYPRESS_DELAY)
        time.sleep(1)

    @staticmethod
    def deploy(pos):
        if pos == 0:
            KI.KeyPress(KI.Q_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.Q_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.Q_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.Q_KEY, KEYPRESS_DELAY)
        elif pos == 1:
            KI.KeyPress(KI.W_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.W_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.W_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.W_KEY, KEYPRESS_DELAY)
        elif pos == 2:
            KI.KeyPress(KI.E_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.E_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.E_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.E_KEY, KEYPRESS_DELAY)
        elif pos == 3:
            KI.KeyPress(KI.R_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.R_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.R_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.R_KEY, KEYPRESS_DELAY)
        elif pos == 4:
            KI.KeyPress(KI.T_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.T_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.T_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.T_KEY, KEYPRESS_DELAY)
        elif pos == 5:
            KI.KeyPress(KI.Y_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.Y_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.Y_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.Y_KEY, KEYPRESS_DELAY)
        elif pos == 6:
            KI.KeyPress(KI.U_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.U_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.U_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.U_KEY, KEYPRESS_DELAY)
        elif pos == 7:
            KI.KeyPress(KI.I_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.I_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.I_KEY, KEYPRESS_DELAY)
            KI.KeyPress(KI.I_KEY, KEYPRESS_DELAY)
        time.sleep(1)
