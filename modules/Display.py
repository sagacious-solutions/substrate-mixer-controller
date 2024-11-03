########################################################################################
## This module is for controlling output to the LCD for shaker
## Docs : https://rplcd.readthedocs.io/en/stable/getting_started.html#initializing-the-lcd
########################################################################################
from multiprocessing import Process
from RPLCD.i2c import CharLCD


class Display :
  def __init__(self, display_config):
    self.config = display_config
    self.config["address"] = int(display_config.get("address", 0x27), 16)
    self.lcdText = ["LCD Initialized..."]
        
    self.lcd = CharLCD(**self.config)

    self.clear_line(0)
    self.write_line(0, self.lcdText[0])

  def write_line(self, line_num, str):
    self.lcd.cursor_pos = (line_num, 0)
    self.lcd.write_string(str)
  

  def clear_line(self, line_num) :
    blank = ""

    for pos in range(self.config.get("cols")) :
      blank += " "

    self.lcd.cursor_pos = (line_num, 0)
    self.lcd.write_string(blank)