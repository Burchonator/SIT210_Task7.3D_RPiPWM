# https://electronicshobbyists.com/raspberry-pi-pwm-tutorial-control-brightness-of-led-and-servo-motor/
# https://www.electronicshub.org/raspberry-pi-ultrasonic-sensor-interface-tutorial/
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18
led_pin = 12
i=0

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)
GPIO.setup(led_pin, GPIO.OUT)
pwm = GPIO.PWM(led_pin, 100)
pwm.start(0)
time.sleep(2)

print("Running")

try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance+1.15, 2)
        print(distance)
        if(distance<=100):
            pwm.ChangeDutyCycle(100-distance)
            time.sleep(0.01)
            print(distance)
        else:
            pwm.ChangeDutyCycle(0) 
        time.sleep(0.1)

except KeyboardInterrupt:
    pwm.stop() 
    GPIO.cleanup()