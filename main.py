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
  

if __name__ == "__main__" :
  main()
  try :
    while True :
      time.sleep(1000)
  finally :
    GPIO.cleanup(18)


