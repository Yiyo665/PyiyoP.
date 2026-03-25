from kivy.app import App
from kivy.uix.label import Label

class ParkingApp(App):
    def build(self):
        return Label(text="Parking PRO funcionando")

ParkingApp().run()
