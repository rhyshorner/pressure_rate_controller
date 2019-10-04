import relays
import time

relays = relays.Relays()
relays.pump_down_relay_off()
relays.pump_up_relay_off()
time.sleep(1)

while True:
	#relays.pump_down_relay_off()
        #relays.pump_up_relay_off()
        relays.pump_down_relay_on()
        #relays.pump_up_relay_on()
        time.sleep(2)

	#relays.pump_down_relay_off()
        #relays.pump_up_relay_off()
        #relays.pump_down_relay_on()
        relays.pump_up_relay_on()
        time.sleep(2)  

        relays.pump_down_relay_off()
        #relays.pump_up_relay_off()
        #relays.pump_down_relay_on()
        #relays.pump_up_relay_on()
        time.sleep(2)

	#relays.pump_down_relay_off()
        relays.pump_up_relay_off()
        #relays.pump_down_relay_on()
        #relays.pump_up_relay_on()
        time.sleep(2)
