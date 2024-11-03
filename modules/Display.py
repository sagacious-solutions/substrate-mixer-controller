########################################################################################
## This module is for controlling output to the LCD for shaker
## Docs : https://rplcd.readthedocs.io/en/stable/getting_started.html#initializing-the-lcd
########################################################################################

from RPLCD.i2c import CharLCD

class Display :
  def __init__(self, display_config):
    display_config["address"] = int(display_config.get("address", 0x27), 16)
    self.lcd = CharLCD(**display_config)

    self.lcd.write_string('New Words world')