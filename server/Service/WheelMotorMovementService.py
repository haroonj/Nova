from gpiozero import Motor
from gpiozero.pins.pigpio import PiGPIOFactory
from Constants import Constants
from server.model.CamMovement import CamMovement
import pygame


class WheelMotorMovementService:
    def __init__(self):
        self.factory = PiGPIOFactory(host=Constants.get_pi_ip_address())
        self.in1_pin = 1
        self.in2_pin = 7
        self.in3_pin = 8
        self.in4_pin = 25

        self.enable1_pin = 24
        self.enable2_pin = 23

        self.in5_pin = 26
        self.in6_pin = 19
        self.in7_pin = 13
        self.in8_pin = 6

        self.enable3_pin = 5
        self.enable4_pin = 0

        #self.motor1 = Motor(forward=1, backward=7, enable=24, pin_factory=self.factory)
        #self.motor2 = Motor(forward=8, backward=25, enable=23, pin_factory=self.factory)
        self.motor3 = Motor(forward=26, backward=19, enable=5, pin_factory=self.factory)
        self.motor4 = Motor(forward=13, backward=6, enable=0, pin_factory=self.factory)

    def forward(self, speed):
        #self.motor1.forward()
        self.motor2.forward()
        self.motor3.forward()
        self.motor4.forward()

    def backward(self, speed):
        self.factory.write(self.in1_pin, True)
        self.factory.write(self.in2_pin, False)
        self.pwm1.ChangeDutyCycle(speed)
        self.factory.write(self.in3_pin, False)
        self.factory.write(self.in4_pin, True)
        self.pwm2.ChangeDutyCycle(speed)
        self.factory.write(self.in5_pin, False)
        self.factory.write(self.in6_pin, True)
        self.pwm3.ChangeDutyCycle(speed)
        self.factory.write(self.in7_pin, True)
        self.factory.write(self.in8_pin, False)
        self.pwm4.ChangeDutyCycle(speed)

    def stop(self):
        #self.motor1.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()

    def move_in_degree(self, cam_movement: CamMovement):
        center_x = cam_movement.x + cam_movement.w / 2
        center_y = cam_movement.y + cam_movement.h / 2
        pan_deg = (center_x - 0) * (1 - -1) / (640 - 0) - 1
        tilt_deg = (center_y - 0) * (1 - -1) / (480 - 0) - 1

        if 0.2 < abs(self.x_pos - pan_deg) < 1:
            self.x_pos = self.x_pos - pan_deg
            self.servo1.value = self.x_pos

        if 0.2 < abs(self.y_pos - tilt_deg) < 1:
            self.y_pos = self.y_pos - tilt_deg
            self.servo2.value = self.y_pos


mC = WheelMotorMovementService()
pygame.init()
screen = pygame.display.set_mode((400, 300))
mC.stop()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            mC.stop()

        elif event.type == pygame.KEYDOWN:
            # Check for arrow keys
            if event.key == pygame.K_UP:
                # Move forward
                mC.forward(100)
            elif event.key == pygame.K_DOWN:
                # Move backward
                mC.reverse(100)
            elif event.key == pygame.K_LEFT:
                # Move backward
                mC.left_turn(100)
            elif event.key == pygame.K_RIGHT:
                # Move backward
                mC.right_turn(100)
            elif event.key == pygame.K_SPACE:
                mC.stop()
            elif event.key == pygame.K_ESCAPE:
                mC.stop()
        else:
            mC.stop()

# def forward(speed):
#     gpio.output(in1_pin, False)
#     gpio.output(in2_pin, True)
#     pwm1.ChangeDutyCycle(speed)
#     gpio.output(in3_pin, True)
#     gpio.output(in4_pin, False)
#     pwm2.ChangeDutyCycle(speed)
#     gpio.output(in5_pin, True)
#     gpio.output(in6_pin, False)
#     pwm3.ChangeDutyCycle(speed)
#     gpio.output(in7_pin, False)
#     gpio.output(in8_pin, True)
#     pwm4.ChangeDutyCycle(speed)
#
#
# def reverse(speed):
#     gpio.output(in1_pin, True)
#     gpio.output(in2_pin, False)
#     pwm1.ChangeDutyCycle(speed)
#     gpio.output(in3_pin, False)
#     gpio.output(in4_pin, True)
#     pwm2.ChangeDutyCycle(speed)
#     gpio.output(in5_pin, False)
#     gpio.output(in6_pin, True)
#     pwm3.ChangeDutyCycle(speed)
#     gpio.output(in7_pin, True)
#     gpio.output(in8_pin, False)
#     pwm4.ChangeDutyCycle(speed)
#
#
# def left_turn(speed):
#     gpio.output(in1_pin, False)
#     gpio.output(in2_pin, True)
#     pwm1.ChangeDutyCycle(speed)
#     gpio.output(in3_pin, False)
#     gpio.output(in4_pin, True)
#     pwm2.ChangeDutyCycle(speed / 2)
#     gpio.output(in5_pin, False)
#     gpio.output(in6_pin, True)
#     pwm3.ChangeDutyCycle(speed)
#     gpio.output(in7_pin, False)
#     gpio.output(in8_pin, True)
#     pwm4.ChangeDutyCycle(speed)
#
#
# def right_turn(speed):
#     gpio.output(in1_pin, True)
#     gpio.output(in2_pin, False)
#     pwm1.ChangeDutyCycle(speed)
#     gpio.output(in3_pin, True)
#     gpio.output(in4_pin, False)
#     pwm2.ChangeDutyCycle(speed)
#     gpio.output(in5_pin, True)
#     gpio.output(in6_pin, False)
#     pwm3.ChangeDutyCycle(speed / 2)
#     gpio.output(in7_pin, True)
#     gpio.output(in8_pin, False)
#     pwm4.ChangeDutyCycle(speed)
#
#
# def stop():
#     pwm1.ChangeDutyCycle(0)
#     pwm2.ChangeDutyCycle(0)
#     pwm3.ChangeDutyCycle(0)
#     pwm4.ChangeDutyCycle(0)
#     gpio.output(in1_pin, False)
#     gpio.output(in2_pin, False)
#     gpio.output(in3_pin, False)
#     gpio.output(in4_pin, False)
#     gpio.output(in5_pin, False)
#     gpio.output(in6_pin, False)
#     gpio.output(in7_pin, False)
#     gpio.output(in8_pin, False)
