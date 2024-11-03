from typing import Dict
import RPi.GPIO as GPIO


class MotorControl :
  def __init__ (self, config: Dict):
    self.pin = config.get("pwm_pin")
    self.speed = config.get("start_speed")
    # Proto Type Code
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.pin, GPIO.OUT) 
    self.pwm = GPIO.PWM(self.pin, 100)
    self.pwm.start(self.speed)

  def run_motor(self, speed = 0) :
    self.pwm.ChangeDutyCycle(speed if speed else self.speed)

  def stop_motor(self) :
    elf.pwm.ChangeDutyCycle(0)