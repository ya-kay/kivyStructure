from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty


## define own classes here
# example

class LoadingScreen(Screen):
    pass

class ExampleScreen(Screen):
    def run(self, name):
        self.parent.current = "loading_screen"
        # change screen from ExampleScreen Class


class MainClass(App):
    ui = Builder.load_file("main.kv")
    
    def build(self):
        return self.ui

    def change_screen(self, screen_name):
        screen_manager = self.root.ids["screen_manager"]
        screen_manager.current = screen_name
        # change screen from App Class


MainClass().run()