from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.config import Config
from kivy.core.window import Window
import login
from login import Status
class Connected(Screen):        

    def disconnect(self):
        stat=login.logout(self.ids['username'].text)
        self.manager.get_screen('login').ids['status'].text=stat.reason
        Window.size = (340, 250)
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()
        