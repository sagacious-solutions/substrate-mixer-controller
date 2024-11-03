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

def main():
  config = load_config(CONFIG_PATH)
  display = Display.Display(config["display"])
  motor = Motor.MotorControl(config["motor"])
  motor.speed = 50
  motor.run_set_time()

  try :
    while True :
      time.sleep(5)
  finally :
    motor.cleanup_gpio()
    
  

if __name__ == "__main__" :
  main()



