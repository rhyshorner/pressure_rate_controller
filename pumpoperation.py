import time
import relays
import MCP3201

#--------------chamber and pump contstraints-------------------
MAX_PRESSURE = 12 #MPa
PUMP_UP_HYSTERISIS = 0.1 #MPa
PUMP_DOWN_HYSTERISIS = 0.1 #MPa
PUMP_HOLD_HYSTERISIS = 0.05 #MPA NOT IMPLEMENTED YET
#---------------------------------------------------------------

class Pumpoperation(object):
    """ Functions for initializing pump control """
    def __init__(self):
        self.relays = relays.Relays()
        self.mcp = MCP3201.MCP3201(0,0)
        self.MAX_PRESSURE = MAX_PRESSURE
        self.PUMP_UP_HYSTERISIS = PUMP_UP_HYSTERISIS
        self.PUMP_DOWN_HYSTERISIS = PUMP_DOWN_HYSTERISIS
        self.PUMP_HOLD_HYSTERISIS = PUMP_HOLD_HYSTERISIS
        self.hysterisis_up_flag = 0
        self.hysterisis_down_flag = 0
        pass

    def pump_actuate(self, moving_setpoint):
        pressure = self.mcp.filtered_pressure()
        if pressure < moving_setpoint:
            self.relays.pump_down_relay_off()
            self.hysterisis_down_flag = 1
            if self.hysterisis_up_flag == 0:
                self.relays.pump_up_relay_on()
            if pressure < (moving_setpoint - self.PUMP_UP_HYSTERISIS):
                self.hysterisis_up_flag = 0
                self.relays.pump_up_relay_on()
        elif pressure >= moving_setpoint:
            self.relays.pump_up_relay_off()
            self.hysterisis_up_flag = 1
            if self.hysterisis_down_flag == 0:
                self.relays.pump_down_relay_on()
            if pressure > (moving_setpoint + self.PUMP_DOWN_HYSTERISIS):
                self.hysterisis_down_flag = 0
                self.relays.pump_down_relay_on()
        print("Pressure is: " + str(pressure) + ", hys up:"+str(self.hysterisis_up_flag) + ", hys down:" + str(self.hysterisis_down_flag))
        return

    def pump_hold_actuate(self, moving_setpoint):
        pressure = self.mcp.filtered_pressure()
        if pressure < moving_setpoint:
            self.relays.pump_down_relay_off()
            self.hysterisis_down_flag = 1
            if self.hysterisis_up_flag == 0:
                self.relays.pump_up_relay_on()
            if pressure < (moving_setpoint - self.PUMP_HOLD_HYSTERISIS):
                self.hysterisis_up_flag = 0
                self.relays.pump_up_relay_on()
        elif pressure >= moving_setpoint:
            self.relays.pump_up_relay_off()
            self.hysterisis_up_flag = 1
            if self.hysterisis_down_flag == 0:
                self.relays.pump_down_relay_on()
            if pressure > (moving_setpoint + self.PUMP_HOLD_HYSTERISIS):
                self.hysterisis_down_flag = 0
                self.relays.pump_down_relay_on()
        print("Pressure is: " + str(pressure) + ", hys up:"+str(self.hysterisis_up_flag) + ", hys down:" + str(self.hysterisis_down_flag))
        return

    def update_pressure(self):
        pressure = self.mcp.filtered_pressure()
#        print("Pressure is: " + str(pressure))
        return pressure


    def end_process(self):
        self.relays.pump_down_relay_off()
        self.relays.pump_up_relay_off()
        return

