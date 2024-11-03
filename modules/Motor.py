import time
from threading import Thread
from typing import Dict
import RPi.GPIO as GPIO

class MotorControl :
  def __init__ (self, config: Dict):
    self.pin = config.get("pwm_pin")
    self.speed = config.get("start_speed")
    self.motor_runtime = config.get("default_run_time")
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.pin, GPIO.OUT) 
    self.pwm = GPIO.PWM(self.pin, 100)

    self.pwm.start(self.speed)

  def run_motor(self, speed = 0) :
    self.pwm.ChangeDutyCycle(speed if speed else self.speed)

  def stop_motor(self) :
    self.pwm.ChangeDutyCycle(0)

  def run_set_time(self, run_time = 0) :
    run_time = run_time if run_time else self.motor_runtime
    print(f"Running motor for {run_time} seconds.")
    self.run_motor(self.speed)
    time.sleep(run_time)
    self.stop_motor()

  # Runs motor for set run time of class without blocking execution thread.
  def run_in_background(self) :
    motor_thread = Thread(target=self.run_set_time)
    motor_thread.start()

  def cleanup_gpio(self) :
    GPIO.cleanup(self.pin)

