from multiprocessing import Process
import modules.Display as Display
import modules.Motor as Motor
import json
import time

CONFIG_PATH = "config.json"

def load_config(path):
  print(f'config loaded from {path}.')

  with open(path) as file :
    config_data = json.load(file)
    return config_data

def count_clock(display):
  count=0
  while True :
    display.lcdText[2] = f"Motor Run time {count}s"
    display.update_line(2)
    count += 1
    time.sleep(1)


def main():
  config = load_config(CONFIG_PATH)
  display = Display.Display(config["display"])
  motor = Motor.MotorControl(config["motor"])
  motor.speed = 100
  motor.run_in_background()

  lcd_process = Process(target=count_clock, args=[display])
  lcd_process.start()

  try :
    time.sleep(10)

  finally :
    motor.cleanup_gpio()
    
  

if __name__ == "__main__" :
  main()



