import wiringpi
import kivy
from kivy.config import Config
kivy.require('1.9.1')

Config.set('kivy', 'exit_on_escape', 1)
Config.set('graphics', 'fullscreen', 0)
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')
Config.write()

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

class Picture(Scatter):
    source = StringProperty(None)

class CamelRaceApp(App):

    pinsToSense = [[8,9,7],[0,2,3],[12,13,14]]

    def __init__(self, **kwargs):
        super(CamelRaceApp, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.gameOver = False

        for idx, pinList in enumerate(self.pinsToSense):
            player = self.getPlayers()[idx]
            for pinIdx, pin in enumerate(pinList):
                wiringpi.pinMode(pin, wiringpi.GPIO.INPUT)
                wiringpi.pullUpDnControl(pin, wiringpi.GPIO.PUD_UP)
                wiringpi.wiringPiISR(pin, wiringpi.GPIO.INT_EDGE_BOTH, lambda x: self.increment(player, 10 * pinIdx))



    def build(self):
        root = self.root #FloatLayout()
        print root.width
        print root.height
        
        self.player1 = Picture(source="images/red.png", pos=(root.width, 700))
        self.player2 = Picture(source="images/blue.png", pos=(root.width, 400))
        self.player3 = Picture(source="images/green.png", pos=(root.width, 100))

        # add to the main field
        root.add_widget(self.player1)
        root.add_widget(self.player2)
        root.add_widget(self.player3)


    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def showWinner(self, player):
        self.gameOver = True
        player.center_x = 1000.0
        player.center_y = 500
        player.scale = 3

    def increment(self, player, amount = 10):
        player.center_x += amount
        if player.center_x >= 1820 and not self.gameOver:
            self.showWinner(player)

    def decrement(self, player, amount= 10):
        player.center_x -= amount

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if self.gameOver:
            return False
        if keycode[1] == '1':
            self.increment(self.player1)
        elif keycode[1] == '2':
            self.increment(self.player2)
        elif keycode[1] == '3':
            self.increment(self.player3)
        elif keycode[1] == 'q':
            self.decrement(self.player1)
        elif keycode[1] == 'w':
            self.decrement(self.player2)
        elif keycode[1] == 'e':
            self.decrement(self.player3)
        return True




if __name__ == '__main__':
    ## Start WiringPi with the WiringPi pin setup
    ## May have to switch to GPIO setup
    wiringpi.wiringPiSetup()
    CamelRaceApp().run()
