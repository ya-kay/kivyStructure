from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


## define own classes here
# example

class LoadingScreen(Screen):
    pass

class ExampleScreen(Screen):
    pass

class MainClass(App):
    ui = Builder.load_file("main.kv")
    
    def build(self):
        return self.ui
    
MainClass().run()