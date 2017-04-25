import wiringpi

# Start WiringPi with the WiringPi pin setup
# May have to switch to GPIO setup
wiringpi.wiringPiSetup()

PIN_TO_SENSE = 8

def gpio_callback():
    print "GPIO_CALLBACK!"

wiringpi.pinMode(PIN_TO_SENSE, wiringpi.GPIO.INPUT)
wiringpi.pullUpDnControl(PIN_TO_SENSE, wiringpi.GPIO.PUD_UP)

wiringpi.wiringPiISR(PIN_TO_SENSE, wiringpi.GPIO.INT_EDGE_BOTH, gpio_callback)

Keep the program running
while True:
    wiringpi.delay(2000)