print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

from kmk.extensions.RGB import RGB
from kmk.modules import Module
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.display import TextEntry
import busio


keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]
keyboard.extensions.append(MediaKeys())


i2c = busio.I2C(scl=board.GP4, sda=board.GP2)

display = Display(
    display=SSD1306(
        i2c=i2c,
        device_address=0x3C
    ),
    width=128,
    height=32
)

def title():
    return "BLENDER"

display.entries = [
    TextEntry(title, x=0, y=0),
    TextEntry("Edit Mode", x=0, y=16),
]

keyboard.extensions.append(display)

encoder_handler.pins = (
    (board.GP8, board.GP7, None, False, 1),
)
encoder_handler.map [ ((KC.VOLD, KC.VOLU, None),),
                     ]

rgb = RGB(pixel_pin=board.GP3, 
          num_pixels=8,
          val_default=80,
          val_limit=255,
          anmation_mode=0
          )
keyboard.extensions.append(rgb)

keyboard.col_pins = (board.GP26, board.GP27, board.GP28,)
keyboard.row_pins = (board.GP29, board.GP6, board.GP7,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

class ReactiveRGB(Module):
    def process_key(self,keyboard, key, is_pressed, int_coord):
        if int_coord is None:
            return key
        
        led = int_coord

        if is_pressed:
            rgb.pixels[led] = (255, 255, 255)
        else:
            rgb.pixels[led] = (80,80,80)
        
        rgb.pixels.show()
        return key
    
keyboard.modules.append(ReactiveRGB())

keyboard.keymap = [ 
    [
        KC.A, KC.B, KC.C, #Dummy keys for testing
        KC.E, KC.F, KC.G,
        KC.D, KC.H, KC.ESC,
    ]
]

if __name__ == '__main__':
    keyboard.go()