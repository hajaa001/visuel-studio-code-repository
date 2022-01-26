import RPi.GPIO as GPIO #Imports the part of the library RPi called GPIO, as just GPIO.
import time #Imports library "time".

#Sets the system of the pi's GPIO-pins to BCM.

GPIO.setmode(GPIO.BCM) #GPIO.setmode sets a mode, BCM is the actual mode. Everything is included in the RPi library. Alternatively, GPIO.BOARD.

#declair GPIO pins
TRIG = 23
ECHO = 24

LED = 25



#Sets up the pins for echo and trig. Must not be set wrong!

GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)




try: #Interrupts the loop when KeyboardInterrupt is true.

    while 1: #True = 1.

        GPIO.output(TRIG, False)
        time.sleep(1)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_Start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_End = time.time()

        duration =pulse_end - pulse_Start
        distance = duration * 17150
        distance = round(distance, 2)

        print ("Disance: ", distance, "cm")

        if distance < 10:
            GPIO.output(LED, True)
        else:
            GPIO.output(LED, False)

        #Stopping the entire program, and resetting the GPIO-pins.

except KeyboardInterrupt: #Triggered when KeyboardInterrupt is true. This interrupts the loop under "try", and runs this loop instead.

        print ("Resetting all GPIO pins to default!")

        #Resetter GPIO-pinnene.

        GPIO.cleanup() #Resets GPIO-pins, fresh start!

        print("Exiting program")
      
    