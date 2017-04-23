from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.config import Config
from kivy.core.window import Window
import login
from login import Status
class Settings(Screen):        

    def back(self):
        Window.size = (340, 250)
        self.manager.transition = SlideTransition(direction="down")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()