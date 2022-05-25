import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)

motion = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
motor = machine.PWM(machine.Pin(16))
motor.freq(1000)

while True:
    if motion.value():
        led_onboard.toggle()
        while motion.value():
            motor.duty_u16(65000)
            utime.sleep(0.001)
        led_onboard.toggle()
        motor.duty_u16(0)