from kivy.app import App
import kivy.metrics
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
# from kivy.properties import StringPropert
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from OBGrammar import Grammar
from OBExpressions import Expressions
from OBLobby import Lobby
from OBModo import Modo
from OBVocabulary import Vocabulary
from Main import UseModes


from kivy.core.window import Window


class ButtonToSort(Button):
    def __init__(self, **kwargs):
        super(ButtonToSort, self).__init__(**kwargs)
    
    def on_release(self):
        print("Button select", Window.size)


class BuildlGUI():

    def __init__(self, sm):
        
        self.sm = sm
        Window.size = (360, 640)
        self.screen_size = Window.size
        
        # Create and add Loby Screen
        self.screen = Screen(name="Lobby")
        # print(self.screen.size_h )
        sm.add_widget(self.screen)
        
        # Create and add Widget in Sceen
        self.widget_navegation = Widget()
        print(self.widget_navegation.size )
        self.screen.add_widget(self.widget_navegation)

        # Create and add BoxLayout in Widget
        # self.layout = StackLayout(orientation='horizontal', )
        self.layout = GridLayout(cols=5, rows=3, row_default_height=(self.screen_size[1]/20), row_force_default=True,
                                 orientation='lr-bt')
        self.screen.add_widget(self.layout)
        # Create and add Buttons in layout
        for i in range(15):
            # self.button1 = Button(text="1", size_hint=(1, 1))# on_click=self.remove())
            if i in [6, 8, 11, 13]:
                button_lvl = ButtonToSort(text=f" ", width=i)
            else:
                button_lvl = ButtonToSort(text=f"{i}")
            self.layout.add_widget(button_lvl)

        # Create and add BoxLayout in Widget
        # self.layout = StackLayout(orientation='horizontal', )
        self.layout = GridLayout(cols=1, rows=1, row_default_height=(self.screen_size[1]/20),
                                row_force_default=True, col_default_width=(self.screen_size[1]/6),
                                col_force_default=True, orientation='tb-lr')
        self.screen.add_widget(self.layout)
        for i in range(1):
            button_lvl = ButtonToSort(text=f"return")
            self.layout.add_widget(button_lvl)

    
    def remove(self):
        print(dir(self.root))
        self.root.clear_widgets()
        return

class Navegation(Screen):
    
    Screen = StringProperty("Lobby")


class Aplication(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.theme_style = "Dark"
        
        # kv = Builder.load_file("display1.kv")
        # https://kivy.org/doc/stable/tutorials/pong.html
        # https://kivy.org/doc/stable/guide/lang.html
        
        sm = ScreenManager()
        BuildlGUI(sm)

        return sm

if __name__ == "__main__":
    randomApp = Aplication()
    randomApp.run()

# sm = ScreenManager()
# sm.add_widget(Lobby(name="Lobby"))
# sm.add_widget(Grammar(name="Grammar"))
# sm.add_widget(Vocabulary(name="Vocabulary"))
# sm.add_widget(Expressions(name="Expressions"))
