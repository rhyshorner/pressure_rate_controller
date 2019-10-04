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

    ramp_time = 600 #seconds
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

    ramp_time = 10 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 1 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 2
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 2 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 600 #seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 2 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 2 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 10 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 2 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 3
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 3 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 600 #seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 3 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 3 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 10 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 3 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 4
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 4 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 600 #seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 4 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 4 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 10 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 4 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 5
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 5 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 600 #seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 5 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 5 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 10 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 5 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 6
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 6 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 600 #seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 6 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 6 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 10 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 6 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 7
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 7 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 600 #seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 7 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 7 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 10 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 7 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 8
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 8 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 600 #seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 8 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 8 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 10 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 8 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 9
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 9 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 600 #seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 9 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 9 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 10 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 9 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #---------------------------------------------------------------------
    #cycle number 10
    ramp_time = 540 #seconds
    start_pressure = 0.15
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 10 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 3600 #seconds
    start_pressure = 5.4
    end_pressure =  5.4
    ramp_sample_rate = 4 #seconds
    cycle_label = 10 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 540 #seconds
    start_pressure = 5.4
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 10 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    ramp_time = 600 #seconds
    start_pressure = 0.15
    end_pressure =  0.15
    ramp_sample_rate = 4 #seconds
    cycle_label = 10 # prints this on debug screen
    ramper.ramp(ramp_time, start_pressure, end_pressure, cycle_label, ramp_sample_rate)

    #-------------------------------------------------------------
    # switches relays off
    ramper.ending_process()

    #--------Extra notes-----------------
    '''
    Tested PN:AS-701 SN: 102, 2019-10-02 
    '''





#--------this makes sure the relays are switched off if the script is interupted-------
except:
    ramper.pumps_off()
    print("a keyboard exception(ctrl+c) or script error occured.")




