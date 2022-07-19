import machine
import Pin as p
import Timer as t

led_onboard = m.Pin(25, m.Pin.OUT)

pwm = m.PWM(m.Pin(16))
pwm.duty_u16(13107)
pwm.freq(440)

# duty cycle goes from 0 to 65025

while True:
    led_onboard.toggle()