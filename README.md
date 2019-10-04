# ramp_pressure_controller
controller for ramp up and ramp down pressure chamber



# pi 3 click shield
    - https://www.mikroe.com/pi-3-click-shield


## 4-20mA Reciever
    - https://github.com/flohwie/raspi-MCP3201/blob/master/MCP3201.py
    - https://www.mikroe.com/4-20ma-r-click


## Relay_click
    - https://www.mikroe.com/relay-click

    - Relay click uses the inbuilt python3 GPIO class, using `RPi.GPIO.setmode(GPIO.BCM)`


## RPI BOOT SETTINGS REQUIRED TO CHANGE
    -   sudo nano /etc/rc.local
        -add "python3 /home/pi/ramp_pressure_controller/off.py &"(line 50) just above `"exit 0"`(line 52)

```
!/bin/sh -e

 rc.local

 This script is executed at the end of each multiuser runlevel.
 Make sure that the script will "exit 0" on success or any other
 value on error.

 In order to enable or disable this script just change the execution
 bits.

 By default this script does nothing.

 Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

python3 /home/pi/ramp_pressure_controller/off.py &

exit 0

```
