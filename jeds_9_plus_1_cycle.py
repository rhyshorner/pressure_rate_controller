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
    cycle_label = 1 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 1800 # 30minute hold, 60seconds*30mins=1800seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 1 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 1 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 30 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 1 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 2
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 2 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 1800 # 30minute hold, 60seconds*30mins=1800seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 2 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 2 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 30 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 2 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 3
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 3 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 1800 # 30minute hold, 60seconds*30mins=1800seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 3 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 3 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 30 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 3 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 4
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 4 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 1800 # 30minute hold, 60seconds*30mins=1800seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 4 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 4 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 30 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 4 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 5
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 5 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 1800 # 30minute hold, 60seconds*30mins=1800seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 5 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 5 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 30 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 5 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 6
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 6 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 1800 # 30minute hold, 60seconds*30mins=1800seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 6 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 6 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 30 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 6 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 7
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 7 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 1800 # 30minute hold, 60seconds*30mins=1800seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 7 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 7 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 30 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 7 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 8
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 8 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 1800 # 30minute hold, 60seconds*30mins=1800seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 8 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 8 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 30 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 8 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 9
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 9 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 1800 # 30minute hold, 60seconds*30mins=1800seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 9 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 9 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 30 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 9 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 10
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 10 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 3600 # 60 minute hold, 60seconds*60mins=3600seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 10 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 10 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 600 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 10 # prints this on terminal
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #-------------------------------------------------------------
    # switches relays off
    ramper.ending_process()

#--------this makes sure the relays are switched off if the script is interupted-------
except:
    ramper.pumps_off()
    print("a keyboard exception(ctrl+c) or script error occured.")

#--------Extra notes-----------------
'''
Script history;
Tested PN:AS-701 SN: 103, 2019-10-15 

document instructions from delivery docket 3654;
Pressure Test 1 PAU Radome.
Pressure testing of the radome with a blank plate no electronics.
Pressurise the radome from 0 to 5.4MPa.
Ramp up/down time is 9 minutes.
Hold for 30minutes at maximum pressure.
Repeat the above for 9 cycles.
30seconds off pressure
Record the actual times and pressure.
On cycle number 10, hold at maximum pressure for 1 hour.
Record results.
Warning do not exceed 5.4MPa
'''