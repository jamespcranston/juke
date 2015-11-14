from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle
from random import random as r
from functools import partial

class JukeboxApp(App):
    
    def build(self): 
        #wid = Widget()


        searchSide = BoxLayout(orientation = 'horizontal')
        Color(1, 0, 0)
        self.search = Button(text='Search', size_hint=(.4, 1))
        self.textbox = TextInput(size_hint_y=.1, multiline=False)
        searchSide.add_widget(self.search)
        searchSide.add_widget(self.textbox)

        queueSide = BoxLayout(orientation = 'horizontal')
        self.queue = Label(text='Queue', size_hint=(.6, 1))
        queueSide.add_widget(self.queue)

        layout = GridLayout(cols = 2)
        layout.add_widget(searchSide)
        layout.add_widget(queueSide)
        return layout


if __name__ == '__main__':
    JukeboxApp().run()


