import RPi.GPIO as GPIO #Imports the part of the library RPi called GPIO, as just GPIO.
import time #Imports library "time".

#Sets the system of the pi's GPIO-pins to BCM.

GPIO.setmode(GPIO.BCM) #GPIO.setmode sets a mode, BCM is the actual mode. Everything is included in the RPi library. Alternatively, GPIO.BOARD.

#declair GPIO pins
TRIG = 23
ECHO = 24

signal = 21



#Sets up the pins for echo and trig. Must not be set wrong!

GPIO.setup(signal, GPIO.IN)




try: #Interrupts the loop when KeyboardInterrupt is true.

    while 1: #True = 1.

        #Stores the input from sensor, and prints it.

        val = GPIO.input(sign  al) #.input reads the input to signal, and this is stored in val.

        print(val) #Prints value in the command prompt.

        time.sleep(0.5) #0.5 seconds delay.



        #Stopping the entire program, and resetting the GPIO-pins.

except KeyboardInterrupt: #Triggered when KeyboardInterrupt is true. This interrupts the loop under "try", and runs this loop instead.

        print ("Resetting all GPIO pins to default!")

        #Resetter GPIO-pinnene.

        GPIO.cleanup() #Resets GPIO-pins, fresh start!

        print("Exiting program")
      
    