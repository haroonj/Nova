from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory

import pygame

factory = PiGPIOFactory(host='192.168.8.107')

servo1 = Servo(10, pin_factory=factory)
servo2 = Servo(9, pin_factory=factory)

pygame.init()
screen = pygame.display.set_mode((400, 300))
running = True
xDutyCycle = 0
yDutyCycle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            factory.close()

        elif event.type == pygame.KEYDOWN:
            # Check for arrow keys
            if event.key == pygame.K_LEFT:
                # Move forward
                servo2.value = 0.8
            elif event.key == pygame.K_RIGHT:
                # Move backward
                servo2.value = -0.8
            elif event.key == pygame.K_UP:
                # Move backward
                servo1.value = -0.8
            elif event.key == pygame.K_DOWN:
                # Move backward
                servo1.value = 0.3
            elif event.key == pygame.K_ESCAPE:
                running = False
                break

