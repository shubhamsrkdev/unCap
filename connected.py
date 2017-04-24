from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.config import Config
from kivy.core.window import Window
import login
from login import Status
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from threading import Thread
from kivy.clock import Clock

class Connected(Screen):   
    def setsize(self,dt):
        Window.size = (340, 250)

    def do_asynclogout(self):
        popup = Popup(title='logging out...', content=Label(text='please wait'),auto_dismiss=False,size_hint=(None, None), size=(200, 100))
        popup.open()
        s=Thread(target=self.disconnect,args=(popup,Window))
        s.start()

    def disconnect(self,popu,win):
        stat=login.logout(self.ids['username'].text)
        popu.dismiss()
        self.manager.get_screen('login').ids['status'].text=stat.reason
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()
        Clock.schedule_once(self.setsize, 0)

    def settings(self):
        Window.size=(340,250)
        self.manager.get_screen('settings').setprev_('connected')
        self.manager.transition = SlideTransition(direction="up")
        self.manager.current = 'settings'             
