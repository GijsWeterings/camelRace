import wiringpi

# Start WiringPi with the WiringPi pin setup
wiringpi.wiringPiSetup()

INPUT_PINS = [1,2,3,4]

for pin in INPUT_PINS:
    wiringpi.pinMode(pin, 0)
