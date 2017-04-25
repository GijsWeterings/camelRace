# import wiringpi
import kivy
from kivy.config import Config
kivy.require('1.9.1')

Config.set('kivy', 'exit_on_escape', 1)
Config.set('graphics', 'fullscreen', 1)
Config.write()

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout

class Picture(Scatter):
    '''Picture is the class that will show the image with a white border and a
    shadow. They are nothing here because almost everything is inside the
    picture.kv. Check the rule named <Picture> inside the file, and you'll see
    how the Picture() is really constructed and used.
    The source property will be the filename to show.
    '''

    source = StringProperty(None)


class CamelRaceApp(App):

    def build(self):
        root = self.root #FloatLayout()
        print root.width
        print root.height
        
        player1 = Picture(source="images/red.png", pos=(root.width, root.height / 2))
        player2 = Picture(source="images/blue.png", pos=(root.width - 200, root.height / 2))
        player3 = Picture(source="images/green.png", pos=(root.width - 300, root.height / 2))

        # add to the main field
        root.add_widget(player1)
        root.add_widget(player2)
        root.add_widget(player3)


if __name__ == '__main__':
    CamelRaceApp().run()
    PIN_TO_SENSE = 23

    ## Start WiringPi with the WiringPi pin setup
    ## May have to switch to GPIO setup
    # wiringpi.wiringPiSetup()

    # def gpio_callback():
    #     print "GPIO_CALLBACK!"

    # wiringpi.pinMode(PIN_TO_SENSE, wiringpi.GPIO.INPUT)
    # wiringpi.pullUpDnControl(PIN_TO_SENSE, wiringpi.GPIO.PUD_UP)

    # wiringpi.wiringPiISR(PIN_TO_SENSE, wiringpi.GPIO.INT_EDGE_BOTH, gpio_callback)

    # Keep the program running
    #while True:
        # wiringpi.delay(2000)