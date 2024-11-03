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
    self.lcdText = [
      "LCD Initialized...",
      "Line sdfklg",
      "Some potato Text",
      "Do Different stuff!!!"      
      ]
        
    self.lcd = CharLCD(**self.config)

    self.update_display()
    print("LCD Initlialization Complete.")

  def update_display(self):
    for i in range(self.config.get("rows")) :
      self.clear_line(i)

      if i >= len(self.lcdText) :
        break

      self.write_line(i, self.lcdText[i])

  def write_line(self, line_num, str):
    max_chars_on_line = self.config.get("cols")

    if len(str) > max_chars_on_line :
      raise ValueError(f"Each row can have no more than {max_chars_on_line} characters.")

    self.lcd.cursor_pos = (line_num, 0)
    self.lcd.write_string(str)  

  def clear_line(self, line_num) :
    blank = ""

    for pos in range(self.config.get("cols")) :
      blank += " "

    self.lcd.cursor_pos = (line_num, 0)
    self.lcd.write_string(blank)