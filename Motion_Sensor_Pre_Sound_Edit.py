import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
pwm = machine.PWM(machine.Pin(16))

pwm.freq(440)

#the pwm is 16 bits so from 0 to 65536


while True:
        led_onboard.toggle()
        pwm.duty_u16(32768)
        # utime.sleep(0)
        led_onboard.toggle()
       