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
    def thread_netcheck(self,dt):
        self.st=Thread(target=self.netcheck)
        self.st.start()
    def netcheck(self):
        import checks
        if not checks.checkSpeed():
            if not checks.checkInternet():
                self.do_autologin('','')
    def start_new_clock(self):
        self.schedule=Clock.schedule_interval(self.thread_netcheck,3)
    def kill_prev_clocks(self):
        try:
            self.schedule.cancel()
            # self.stop_th.set()
        except:
            print("no previous schedule")
    def do_autologin(self,usr,pwd):
        popup = Popup(title='logging in...',content=Label(text='please wait'),auto_dismiss=False,size_hint=(None, None), size=(200, 100))
        popup.open()
        s=Thread(target=self.autoLogin,args=(usr,popup))
        s.start()             

    def autoLogin(self,usr,popu):
        creds={}
        with open('cred.bin','rb') as f:
            from pickle import load
            creds=load(f)
        if usr != '':
            try:
                if login.login(usr,creds[usr]).success:
                    popu.dismiss()
                    self.kill_prev_clocks()
                    self.start_new_clock()
                    if (self.manager.current=='connected' or self.manager.current=='login'):
                        Clock.schedule_once(self.setsize, 0)
                        self.manager.transition = SlideTransition(direction="left")
                        self.manager.current = 'connected'
                    self.manager.get_screen("connected").ids['username'].text = username
                    return
            except:
                print("error occured with provided user")           
        for username in creds.keys():
            popu.content=Label(text=username)
            if login.login(username,creds[username]).success:
                try:
                    self.kill_prev_clocks()
                except:
                    print("no prev clocks running")
                popu.dismiss()
                self.start_new_clock()
                if (self.manager.current=='connected' or self.manager.current=='login'):
                        Clock.schedule_once(self.setsize, 0)
                        self.manager.transition = SlideTransition(direction="left")
                        self.manager.current = 'connected'
                self.manager.get_screen("connected").ids['username'].text = username
                return
            else:
                pass                
        self.ids['status'].text="autologin failed"
        popu.dismiss()
                

    def setsize(self,dt): 
        Window.size=(340,150)
    def do_asynclogin(self,username,password):
        if username == '' or password == '':
            self.do_autologin(username,password)
        popup = Popup(title='logging in...', content=Label(text='please wait'),auto_dismiss=False,size_hint=(None, None), size=(200, 100))
        popup.open()
        s=Thread(target=self.do_login,args=(username,password,popup))
        s.start()
        
        # s.join()S
    def do_login(self, username, password,popu):
        #self.ids['status'].color=[1,1,1,1]
        self.ids['status'].text="enter username and password"
        if((username or password) == ''):
            self.ids['status'].text="username and password cannot be blank"
            #self.ids['status'].color=[1,0,0,1]
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
    title='unCap by Uday'

    def build(self):
        try:
            with open('cred.bin','rb') as f:
                pass
        except:
            try:
                with open('cred.bin','wb') as f:
                    a={'user':'password'}
                    from pickle import dump
                    dump(a,f)
            except:
                print("i don't have write access")
        self.icon='res/icon.png'
        manager = ScreenManager()
        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        manager.add_widget(Settings(name='settings'))
        # manager.add_widget(CredMan(name='credman'))

        return manager

    def get_application_config(self):
        print("hello")
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
