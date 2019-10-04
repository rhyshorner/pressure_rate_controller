import time
import ramping_procedure
ramper = ramping_procedure.RampingProcedure()
try:
#Comment out "ramper.create_csv()" line to disable csv's
    ramper.create_csv()
    input("press enter to begin test procedure.")



#------------------------------------------------------------------------
#----------SCRIPT HERE--------------------------------------------------
#-----------------------------------------------------------------------

    ramper.prime_pressure_chamber()
    #---------------------------------------------------------------------
    #cycle number 1
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 1 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 28800 # 28800seconds = 8hours
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 1 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 1 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 600 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 1 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #-------------------------------------------------------------
    # switches relays off
    ramper.ending_process()

    #--------Extra notes-----------------
    '''
    Tested PN:AS-701 SN: 101, 2019-10-03 
    '''





#--------this makes sure the relays are switched off if the script is interupted-------
except:
    ramper.pumps_off()
    print("a keyboard exception(ctrl+c) or script error occured.")


