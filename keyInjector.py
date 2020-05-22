import ctypes
import time

# This class handles keyboard input to the emulator

# HEX codes link: http://www.flint.jp/misc/?q=dik&lang=en
##############
ENTER = 0x1C
ALT = 0x38  # is left alt
SPACE_BAR = 0x39

KEY1 = 0x02
KEY2 = 0x03
KEY3 = 0x04
KEY4 = 0x05
KEY5 = 0x06
KEY6 = 0x07
KEY7 = 0x08
KEY8 = 0x09
KEY9 = 0x0A
KEY0 = 0x0B
TILDE_LOWER = 0x29

Q_KEY = 0x10
W_KEY = 0x11
E_KEY = 0x12
R_KEY = 0x13
T_KEY = 0x14
Y_KEY = 0x15
U_KEY = 0x16
I_KEY = 0x17
O_KEY = 0x18
P_KEY = 0x19
LBRACKET = 0x1A
RBRACKET = 0x1B

A_KEY = 0x1E
S_KEY = 0x1F
D_KEY = 0x20
F_KEY = 0x21
G_KEY = 0x22
H_KEY = 0x23
J_KEY = 0x24
K_KEY = 0x25
L_KEY = 0x26
SEMICOLON_KEY = 0x27

Z_KEY = 0x2C
X_KEY = 0x2D
C_KEY = 0x2E
V_KEY = 0x2F
B_KEY = 0x30
N_KEY = 0x31
M_KEY = 0x32
COMMA_KEY = 0x33
DOT_KEY = 0x34
F_SLASH_KEY = 0x35

NUMPAD_0 = 0x52
NUMPAD_1 = 0x4F
NUMPAD_2 = 0x50
NUMPAD_3 = 0x51
NUMPAD_4 = 0x4B
NUMPAD_5 = 0x4C
NUMPAD_6 = 0x4D
NUMPAD_7 = 0x47
NUMPAD_8 = 0x48
NUMPAD_9 = 0x49

#####
SAFE_DELAY = 1
SHORT_DELAY = .7
DELAY = .75
TYPE_DELAY = .2
NO_DELAY = .05
FAST = .5

# This code is not originally mine, and I unfortunately do not know the original author
# This "C" code is required to emulate the low-level keystrokes required by modern emulators
# (e.g. get around DirectInput)
# Link in which I found the code:
# https://www.reddit.com/r/learnpython/comments/22tke1/use_python_to_send_keystrokes_to_games_in_windows/
SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions


def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def KeyPress(keycode, delay=DELAY):
    time.sleep(delay)
    PressKey(keycode)
    time.sleep(0.05)
    ReleaseKey(keycode)
