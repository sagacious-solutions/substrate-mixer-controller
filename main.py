from multiprocessing import Process
import modules.Display as Display
import json
import time
import RPi.GPIO as GPIO

# Proto Type Code
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) 
pwm = GPIO.PWM(18, 100)
pwm.start(100)  # Start with 0% duty cycle (LED off


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


