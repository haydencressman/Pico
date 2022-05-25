import machine
import utime


led_onboard = machine.Pin(25, machine.Pin.OUT)
pwm = machine.PWM(machine.Pin(16))

# there will be more, and in fact probably just gonna use two picos to do this

#--------------- tonal area ----------------------
btone = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)
bflattone = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
atone = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_DOWN)
aflattone = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)
gtone = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

tones = [494, 466, 440, 415, 392]



#the tones are in order from [B Bb A Ab G]



#the pwm duty is 16 bits so from 0 to 65536, this just controls volume, anything above 50% is absolutely ear shattering

#-------------- slide pot area ---------------
#slide_pot = machine.ADC(28)
pwm.duty_u16(13107)

while True:
    #reading = slide_pot.read_u16()
    
    led_onboard.toggle()
    if btone.value():
        pwm.duty_u16(13107)
        pwm.freq(494)
        utime.sleep(.01)
    elif bflattone.value():
        pwm.duty_u16(13107)
        led_onboard.toggle()
        pwm.freq(466)
        utime.sleep(.01)
    elif atone.value():
        pwm.duty_u16(13107)
        led_onboard.toggle()
        pwm.freq(440)
        utime.sleep(.01)
    elif aflattone.value():
        pwm.duty_u16(13107)
        led_onboard.toggle()
        pwm.freq(415)
        utime.sleep(.01)
    elif gtone.value():
        pwm.duty_u16(13107)
        led_onboard.toggle()
        pwm.freq(392)
        utime.sleep(.01)
    else:
        pwm.duty_u16(0)
        utime.sleep(.001)
        
    # utime.sleep(0)
    led_onboard.toggle()
       
