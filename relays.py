import RPi.GPIO as GPIO
import time

PUMP_UP_RELAY = 17
PUMP_DOWN_RELAY = 7

class Relays(object):
    """Functions for initializing pi click relays and controlling them """
    def __init__(self):
        self.PUMP_UP_RELAY = PUMP_UP_RELAY
        self.PUMP_DOWN_RELAY = PUMP_DOWN_RELAY

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.PUMP_UP_RELAY, GPIO.OUT)
        GPIO.setup(self.PUMP_DOWN_RELAY, GPIO.OUT)
        GPIO.output(self.PUMP_UP_RELAY, GPIO.LOW)
        GPIO.output(self.PUMP_DOWN_RELAY, GPIO.LOW)

    def pump_up_relay_on(self):
        GPIO.output(self.PUMP_UP_RELAY, GPIO.HIGH)
#        print("pump up relay is: ON")
        return

    def pump_up_relay_off(self):
        GPIO.output(self.PUMP_UP_RELAY, GPIO.LOW)
#        print("pump up relay is: OFF")
        return

    def pump_down_relay_on(self):
        GPIO.output(self.PUMP_DOWN_RELAY, GPIO.HIGH)
#        print("pump down relay is: ON")
        return

    def pump_down_relay_off(self):
        GPIO.output(self.PUMP_DOWN_RELAY, GPIO.LOW)
#        print("pump down relay is: OFF")
        return
