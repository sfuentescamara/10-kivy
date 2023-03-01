from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from create_gui import BuildlGUI
from modes import Mode

class Aplication(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.theme_style = "Dark"
        
        # kv = Builder.load_file("display1.kv")
        # https://kivy.org/doc/stable/tutorials/pong.html
        # https://kivy.org/doc/stable/guide/lang.html
        
        logic = Mode()
        ui = ScreenManager()
        BuildlGUI(ui, logic)

        return ui
    

if __name__ == "__main__":
    randomApp = Aplication()
    randomApp.run()