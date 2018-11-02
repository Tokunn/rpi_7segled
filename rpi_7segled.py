#!/usr/bin/env python3

import pigpio
import time

PIN_CLK   = 17  # 11
PIN_DATA  = 27  # 13
PIN_LATCH = 22  # 15

pi = pigpio.pi()
pi.set_mode(PIN_CLK, pigpio.OUTPUT)
pi.set_mode(PIN_DATA, pigpio.OUTPUT)
pi.set_mode(PIN_LATCH, pigpio.OUTPUT)

pi.write(PIN_CLK, 0)
pi.write(PIN_DATA, 0)
pi.write(PIN_LATCH, 1)

t = 0.0005

while True:
    print("Send")
    bit_char = 0x61
    for i in range(8):
        clk = 0
        output = (bit_char & 0b10000000) >> 7
        print(output)
        bit_char = bit_char << 1
        time.sleep(t)

        clk = 1
        time.sleep(t)
    time.sleep(1)
