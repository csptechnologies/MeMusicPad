import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())
keyboard = KMKKeyboard()
keyboard.matrix = KeysScanner(
    pins=[board.D10, board.D9, board.D8, board.D0, board.D6, board.D1],
)
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D2, board.D3, None, False),)
keyboard.modules.append(encoder_handler)

# DO OLED LATER

keyboard.keymap = [
    [
        KC.MPREV, KC.MPLY, KC.MNXT, KC.MSTP, KC.F13,
    ]
]


encoder_handler.map = [
    (
        (KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP),
    )
]

if __name__ == '__main__':
    keyboard.go()