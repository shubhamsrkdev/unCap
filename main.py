from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
from kivy.config import Config
import login
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.clock import Clock


from connected import Connected
from settings import Settings
from threading import Thread


Config.set('graphics', 'width', '340')
Config.set('graphics', 'height', '250')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
#Config.set('graphics', 'borderless', '1')

class Login(Screen):
    def setsize(self,dt): 
        Window.size=(340,150)
    def do_asynclogin(self,username,password):
        popup = Popup(title='logging in...', content=Label(text='please wait'),auto_dismiss=False,size_hint=(None, None), size=(200, 100))
        popup.open()
        s=Thread(target=self.do_login,args=(username,password,popup))
        s.start()
        
        # s.join()S
    def do_login(self, username, password,popu):
        self.ids['status'].color=[1,1,1,1]
        self.ids['status'].text="enter username and password"
        if((username or password) == ''):
            self.ids['status'].text="username and password cannot be blank"
            self.ids['status'].color=[1,0,0,1]
            popu.dismiss()
            return
        app = App.get_running_app()
        stat=login.login(username,password)
        popu.dismiss()
        if(stat.success):
            Clock.schedule_once(self.setsize, 0)
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'connected'
            self.manager.get_screen("connected").ids['username'].text = self.ids['login'].text
            app.config.read(app.get_application_config())
            app.config.write()
        else:
            self.ids['status'].text=stat.reason
    
    def settings(self):
        self.manager.transition = SlideTransition(direction="up")
        self.manager.current = 'settings'
        self.manager.get_screen('settings').setprev_('login')

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""
    
    def getusername(self):
        return self.ids['login'].text

    def exit(self):
        exit()

class LoginApp(App):
    Window.size = (350, 225)
    username = StringProperty(None)
    password = StringProperty(None)
    title='Cyberoam Login <3 Uday'

    def build(self):
        self.icon='icon.png'
        manager = ScreenManager()
        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        manager.add_widget(Settings(name='settings'))

        return manager

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )

if __name__ == '__main__':
    LoginApp().run()
