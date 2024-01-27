from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

import pygame

from Constants import Constants

#from Constants import Constants

factory = PiGPIOFactory(host=Constants.get_pi_ip_address())

servo1 = Servo(9, pin_factory=factory)
servo2 = Servo(10, pin_factory=factory)

pygame.init()
screen = pygame.display.set_mode((400, 300))
running = True
xDutyCycle = 0
yDutyCycle = 0
servo1.value = yDutyCycle
servo2.value = xDutyCycle
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            factory.close()

        elif event.type == pygame.KEYDOWN:
            # Check for arrow keys
            if event.key == pygame.K_LEFT:
                # Move forward
                if xDutyCycle != 0.8:
                    xDutyCycle = xDutyCycle + 0.05
                    servo2.value = xDutyCycle
            elif event.key == pygame.K_RIGHT:
                # Move backward
                if xDutyCycle != -0.8:
                    xDutyCycle = xDutyCycle - 0.05
                    servo2.value = xDutyCycle
            elif event.key == pygame.K_DOWN:
                # Move backward
                if yDutyCycle != -0.35:
                    yDutyCycle = yDutyCycle - 0.05
                    servo1.value = yDutyCycle
            elif event.key == pygame.K_UP:
                # Move backward
                if yDutyCycle != 0.75:
                    yDutyCycle = yDutyCycle + 0.05
                    servo1.value = yDutyCycle
            elif event.key == pygame.K_SPACE:
                # Move backward
                servo1.mid()
                servo2.mid()
            elif event.key == pygame.K_ESCAPE:
                factory.close()
                running = False
                break

