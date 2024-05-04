from gpiozero import Motor
from gpiozero.pins.pigpio import PiGPIOFactory
from Constants import Constants
from server.model.CamMovement import CamMovement
import pygame

factory = PiGPIOFactory(host=Constants.get_pi_ip_address())

motor = Motor(forward=8, backward=25, pwm=True, pin_factory=factory)

# Set the speed of the motor
motor.value = 0.5

# Move the motor forward
motor.forward()

# Stop the motor
motor.stop()
