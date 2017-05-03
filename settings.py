from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.config import Config
from kivy.core.window import Window
import login
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from login import Status

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout


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
    
    def cred(self):
        Window.size=(340,500)
        creds={}
        credman=Screen(name='credman',id='screen')
        base=BoxLayout(padding=[0,0,0,0],orientation='vertical',id='base',size_hint_y=None,height=500)
        buttons=BoxLayout(padding=[0,0,0,0],orientation='horizontal',id='buttons',height=450)
        buttons.add_widget(Button(text= 'add',font_size= 15,pos=[40, 40],size_hint=[1, None],height=30,on_press=lambda x:self.p_add(credman)))
        buttons.add_widget(Button(text= 'save',font_size= 15,pos=[40, 40],size_hint=[1, None],height=30,on_press=lambda x:self.c_save(credman)))
        buttons.add_widget(Button(text= 'back',font_size= 15,pos=[40, 40],size_hint=[1, None],height=30,on_press=lambda x:self.c_back(credman)))
        print('yolo')
        with open('cred.bin','rb') as f:
            from pickle import load
            creds=load(f)
        i=0
        layout=GridLayout(cols=1,size_hint=[1,None],height=450)
        # layout.bind(minimum_height=layout.setter('height'))
        for user in creds.keys():
            print(user)
            usr=TextInput(text=str(user),id=str(str(i)+'u'),multiline=False,write_tab=False,use_bubble=True,size_hint=[1, None],height=35)
            pwd=TextInput(text=str(creds[user]),id=str(str(i)+'p'),multiline=False,write_tab=False,password=True,use_bubble=True,size_hint=[1, None],height=35)
            dele=Button(text=str('x'),size_hint=[None,1],width=20,id=str(i),on_press=lambda i:self.c_dele(credman,i.id),height=35)
            lay=BoxLayout(orientation='horizontal',id=str(i))
            lay.add_widget(usr)
            lay.add_widget(pwd)
            lay.add_widget(dele)
            layout.add_widget(lay)
            i=i+1
        layout.height=i*35
        sc=ScrollView(id='list',size_hint=[1,None],height=470)
        sc.add_widget(layout)
        base.add_widget(sc)
        base.add_widget(buttons)
        credman.add_widget(base)
        self.manager.add_widget(credman)
        self.manager.current='credman'

    def about(self):
        popup = Popup(title='Made by Uday.', content=Label(text='click outside the box to dismiss',font_size='9sp'),auto_dismiss=True,size_hint=(None, None), size=(200, 100),title_size='20sp',title_align='center')
        popup.open()

    def c_back(self,screen):
        Window.size = (340, 250)
        self.manager.remove_widget(self.manager.get_screen('credman'))
        self.manager.current='settings'

    def c_save(self,credman):
        creds={}
        with open('cred.bin','rb') as f:
            from pickle import load
            creds=load(f)
        i=0
        wid={}
        for widget in self.manager.get_screen('credman').walk():
            wid[widget.id]=widget
        print(wid)
        new_creds={}
        for keys in creds.keys():
            new_creds[wid[str(i)+'u'].text]=str(wid[str(i)+'p'].text)
            i=i+1
        with open('cred.bin','wb') as f:
            from pickle import dump
            dump(new_creds,f)         
        self.c_back(credman)
        self.cred()
    
    def c_dele(self,credman,id):
        creds={}
        with open('cred.bin','rb') as f:
            from pickle import load
            creds=load(f)
        i=0
        wid={}
        for widget in self.manager.get_screen('credman').walk():
            wid[widget.id]=widget
        print(wid)
        new_creds={}
        for keys in creds.keys():
            if str(i)==id:
                i=i+1
                continue
            else:
                new_creds[wid[str(i)+'u'].text]=str(wid[str(i)+'p'].text)
            i=i+1
        with open('cred.bin','wb') as f:
            from pickle import dump
            dump(new_creds,f)         
        self.c_back(credman)
        self.cred()
        
    def p_add(self,credman):
        base=BoxLayout(orientation="vertical",id="box")
        user=TextInput(id="user",hint_text="username",multiline=False,write_tab=False,use_bubble=True)
        pwd=TextInput(id="user",hint_text="password",multiline=False,write_tab=False,use_bubble=True,password=True)
        add=Button(id="add",text="add",on_press=lambda x:self.c_add(user,pwd))
        quit=Label(text='click outside the box to dismiss',font_size='9sp')
        base.add_widget(user)
        base.add_widget(pwd)
        base.add_widget(add)
        base.add_widget(quit)
        popup = Popup(title='Add User', content=base,auto_dismiss=True,size_hint=(None, None), size=(200, 200),title_size='20sp',title_align='center')
        popup.open()

    def c_add(self,username,password):
        if username == '' or password == '':
            return
        creds={}
        with open('cred.bin','rb') as f:
            from pickle import load
            creds=load(f)
        creds[username.text]=password.text
        with open('cred.bin','wb') as f:
            from pickle import dump
            dump(creds,f)
        username.text=''
        password.text=''
        self.c_back(credman)
        self.cred()
        