from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty

from OBGrammar import Grammar
from OBExpressions import Expressions
from OBLobby import Lobby
from OBModo import Modo
from OBVocabulary import Vocabulary

class WindowMain(ScreenManager):
    pass

class Aplication(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.theme_style = "Dark"
        kv = Builder.load_file("display.kv")
        
        return kv

    # def on_stop(self):
    #     randomApp.stop()

if __name__ == "__main__":
    randomApp = Aplication()
    randomApp.run()

sm = ScreenManager()
sm.add_widget(Lobby(name="Lobby"))
sm.add_widget(Grammar(name="Grammar"))
sm.add_widget(Vocabulary(name="Vocabulary"))
sm.add_widget(Expressions(name="Expressions"))
