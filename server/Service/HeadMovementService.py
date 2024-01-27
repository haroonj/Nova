from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from Constants import Constants
from server.model.CamMovement import CamMovement


class HeadMovementService:
    def __init__(self, servo_pin1, servo_pin2):
        self.factory = PiGPIOFactory(host=Constants.get_pi_ip_address())

        self.servo1 = Servo(servo_pin1, pin_factory=self.factory)
        self.servo2 = Servo(servo_pin2, pin_factory=self.factory)

        self.x_pos = 0
        self.y_pos = 0

    def move_to(self, x, y):
        self.servo1.value = x
        self.servo2.value = y

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

