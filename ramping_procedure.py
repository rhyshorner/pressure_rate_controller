import time
import datetime
import pumpoperation
import csv

PUMP_SPEED = 1 # seconds
prime_speed = 1

class RampingProcedure(object):

    def __init__(self):
        self.pumper = pumpoperation.Pumpoperation()
        self.PUMP_SPEED = PUMP_SPEED
        self.prime_countdown_timer = time.time()
        self.prime_speed = prime_speed
        self.csvfilename = ""
        self.pressure_for_csv = 0
        self.moving_setpoint_for_csv = 0
        pass

# need to modify this as hold ramp to 0.1
    def prime_pressure_chamber(self, moving_setpoint=0.2):
        self.moving_setpoint_for_csv = moving_setpoint
        print("pressure profile: " + str(moving_setpoint))
        pressure = self.pumper.update_pressure()
        while pressure <= moving_setpoint:
            self.pumper.update_pressure() 
            if (time.time() - self.prime_countdown_timer) >= self.prime_speed:
                self.prime_countdown_timer = time.time()

                self.pressure_for_csv = self.pumper.update_pressure()
                self.moving_setpoint_for_csv = moving_setpoint
                self.update_csv()
                
                self.pumper.pump_actuate(moving_setpoint)
                pressure = self.pumper.update_pressure()

            self.pumper.update_pressure()
           
        print("pressure chamber priming sequence completed.")
        return

    def ramp(self, ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate=5):
        pressure_difference = end_pressure - start_pressure
        ramp_number_of_steps = ramp_time / ramp_sample_rate # total time/step time
        step_size = round(pressure_difference / ramp_number_of_steps, 4) #total pressure/step
        moving_setpoint = start_pressure

        sample_rate_countdown_timer = time.time()
        pump_speed_countdown_timer = time.time()

        print("")
        print("cycle number: " + str(cycle_label))
        print("next ramp procedure initiated...")
        #print("ramp_time:"+str(ramp_time)+", ramp_sample_rate:"+str(ramp_sample_rate))
        #print("ramp_number_of_steps:"+str(ramp_number_of_steps) + ", moving_setpoint:"+str(moving_setpoint) + ", step_size:"+str(step_size))
        #print("start_pressure:"+str(start_pressure)+", end_pressure:"+str(end_pressure) + ", pressure_difference: " + str(pressure_difference))
        print("")

        if step_size > 0:
            print("Cycle number: " + str(cycle_label) + ", Pressure profile: " + str(moving_setpoint))
            self.pumper.update_pressure()
            if (time.time() - pump_speed_countdown_timer) >= self.PUMP_SPEED:
                pump_speed_countdown_timer = time.time()
                self.pumper.update_pressure()
                self.pumper.pump_actuate(moving_setpoint)
                self.pressure_for_csv = self.pumper.update_pressure()
                self.moving_setpoint_for_csv = moving_setpoint
                self.update_csv()

            while moving_setpoint < end_pressure:
                self.pumper.update_pressure()
                if (time.time() - sample_rate_countdown_timer) >= ramp_sample_rate:
                    sample_rate_countdown_timer = time.time()
                    moving_setpoint = round(moving_setpoint + step_size, 4)
                    self.pumper.update_pressure()
                    print("Cycle number: " + str(cycle_label) + ", Pressure profile: " + str(moving_setpoint))

                if (time.time() - pump_speed_countdown_timer) >= self.PUMP_SPEED:
                    pump_speed_countdown_timer = time.time()
                    self.pumper.update_pressure()
                    self.pumper.pump_actuate(moving_setpoint)
                    self.pressure_for_csv = self.pumper.update_pressure()
                    self.moving_setpoint_for_csv = moving_setpoint
                    self.update_csv()

            time.sleep(ramp_sample_rate)

        elif step_size < 0:
            print("Cycle number: " + str(cycle_label) + ", Pressure profile: " + str(moving_setpoint))
            self.pumper.update_pressure()
            if (time.time() - pump_speed_countdown_timer) >= self.PUMP_SPEED:
                pump_speed_countdown_timer = time.time()
                self.pumper.update_pressure()
                self.pumper.pump_actuate(moving_setpoint)
                self.pressure_for_csv = self.pumper.update_pressure()
                self.moving_setpoint_for_csv = moving_setpoint
                self.update_csv()

            while moving_setpoint > end_pressure:
                self.pumper.update_pressure()
                if (time.time() - sample_rate_countdown_timer) >= ramp_sample_rate:
                    sample_rate_countdown_timer = time.time()
                    moving_setpoint = round(moving_setpoint + step_size, 4)
                    self.pumper.update_pressure()
                    print("Cycle number: " + str(cycle_label) + ", Pressure profile: " + str(moving_setpoint))

                if (time.time() - pump_speed_countdown_timer) >= self.PUMP_SPEED:
                    pump_speed_countdown_timer = time.time()
                    self.pumper.update_pressure()
                    self.pumper.pump_actuate(moving_setpoint)
                    self.pressure_for_csv = self.pumper.update_pressure()
                    self.moving_setpoint_for_csv = moving_setpoint
                    self.update_csv()

            self.pumper.update_pressure()
            time.sleep(ramp_sample_rate)

        elif step_size == 0:
            print("Cycle number: " + str(cycle_label) + ", Pressure profile: " + str(moving_setpoint) + ", Time left to hold: " + str(ramp_time))
            self.pumper.update_pressure()
            countdown_timer = time.time()
            while ramp_time > 0:
                self.pumper.update_pressure()
                if (time.time() - sample_rate_countdown_timer) >= ramp_sample_rate:
                    sample_rate_countdown_timer = time.time()
                    ramp_time = ramp_time - ramp_sample_rate
                    self.pumper.update_pressure()
                    print("Cycle number: " + str(cycle_label) + ", Pressure profile: " + str(moving_setpoint) + ", Time left to hold: " + str(ramp_time))

                if (time.time() - pump_speed_countdown_timer) >= self.PUMP_SPEED:
                    pump_speed_countdown_timer = time.time()
                    self.pumper.update_pressure()
                    self.pumper.pump_hold_actuate(moving_setpoint)
                    #self.pumper.pump_actuate(moving_setpoint)
                    self.pressure_for_csv = self.pumper.update_pressure()
                    self.moving_setpoint_for_csv = moving_setpoint
                    self.update_csv()
            self.pumper.update_pressure()        
            time.sleep(ramp_sample_rate)
        return

    def pumps_off(self):
        self.pumper.end_process()   
        print("Pump relays have been de-energized.")
        return

    def ending_process(self):
        self.pumper.end_process()   
        print("ending process complete.")
        return

    def create_csv(self):
        print("")
        print("Note that the current date and time will automatically be added to the filename.")
        userfilename = input("what would you like to name this csv file?")
        filetimestamp = "{:%Y-%m-%d_%H-%M-%S}".format(datetime.datetime.now())
        self.csvfilename = "/home/pi/ramp_pressure_controller/csvfiles/" + str(userfilename) + "_" + filetimestamp + ".csv"
        f = open(self.csvfilename, 'w', newline='')
        writer = csv.writer(f)
        writer.writerow(['Date', 'Time', 'Profile', 'Pressure'])
        # closes the file
        f.close()
        return

    def update_csv(self):
        try:
            timestampdate = "{:%Y-%m-%d}".format(datetime.datetime.now())
            timestamptime = "{:%H:%M:%S}".format(datetime.datetime.now())
            with open(self.csvfilename, mode='a', newline='') as f:
                csv.writer(f, delimiter=',').writerow([timestampdate, timestamptime, self.moving_setpoint_for_csv, self.pressure_for_csv])
                f.close()
        except:
            pass
        return
