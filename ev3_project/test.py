#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
# import requests
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.led import Leds

print('Hello!')

ir = InfraredSensor()
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
leds = Leds()

thresh = 18

def remove_ad(prox):
    while True:
        if prox < thresh:
            leds.set_color("LEFT", "RED")
            leds.set_color("RIGHT", "RED")
            tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 5)
        else:
            leds.set_color("LEFT", "GREEN")
            leds.set_color("RIGHT", "GREEN")
            return
        prox = ir.proximity
        print('step 2', prox)
        time.sleep(1.0)
        if prox == 0 or prox == 100:
            prox = thresh - 1

def deliver_mail():
    pass

def is_ad():
    return True

while True:
    prox = ir.proximity
    print('step 1', prox)
    time.sleep(1.0)
    if prox == 0 or prox == 100:
        continue
    if prox < thresh:
        if is_ad():
            # 広告だった
            remove_ad(prox)
        else:
            # 郵便物だった
            deliver_mail()
