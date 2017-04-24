from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.config import Config
from kivy.core.window import Window
import login
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from login import Status
class Settings(Screen):        
    def __init__(self,**kwargs):
        super(Screen,self).__init__(**kwargs)
        #self.prev=''

    def setprev_(self,prev):
        self.prev=prev
        
                
    def back(self):
        if self.prev=='login':
            Window.size = (340, 250)
        if self.prev=='connected':
            Window.size = (340, 150)
        self.manager.transition = SlideTransition(direction="down")
        self.manager.current = self.prev

    def about(self):
        popup = Popup(title='Made by Uday.', content=Label(text='click outside the box to dismiss',font_size='9sp'),auto_dismiss=True,size_hint=(None, None), size=(200, 100),title_size='20sp',title_align='center')
        popup.open()
        
