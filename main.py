from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from time import strftime

class DigitalClock(Label):
    def __init__(self, **kwargs):
        super(DigitalClock, self).__init__(**kwargs)
        self.font_size = '36dp'  # Set font size to medium-large
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        self.text = strftime('%H:%M:%S %p')

class DigitalClockApp(App):
    def build(self):
        return DigitalClock()

if __name__ == '__main__':
    DigitalClockApp().run()
