from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget

from kivy.uix.label import Label

from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import MDList
from kivymd.uix.scrollview import MDScrollView

from button_handler import button_handler
from config import MODES, WINDOWS_SIZE

class ScrollList(MDScrollView):
    def __init__(self, **kwargs):
        super(ScrollList, self).__init__(MDList(id="container"),**kwargs)

class ListMenu(OneLineListItem):
    def __init__(self, current_gui, *args, **kwargs):
        self.current_screen = current_gui
        super().__init__(*args, **kwargs)

    def on_release(self):
        super().on_release()
        button_handler(self, self.current_screen)

class ButtonToSort(Button):
    def __init__(self, current_gui, **kwargs):
        self.current_screen = current_gui

        super(ButtonToSort, self).__init__(**kwargs)
    
    def on_release(self):
        button_handler(self, self.current_screen)


class BuildlGUI:
    """
    This class creates the graphical user interface in the sm object

    Args:
        ui: ScreenManager instance to add screens and widgets
        logic: Mode instance to storage data

    Returns:
        None
    """

    def __init__(self, ui: object, logic: object):
        
        Window.size = WINDOWS_SIZE
        self.screen_size = Window.size
        self.logic = logic
        
        # Create and add Loby Screen
        self.screen = Screen(name="Lobby")
        ui.add_widget(self.screen)
        self.lobby_ui()
        
    def lobby_ui(self):
        # Create and add Widget in Sceen
        self.widget_lobby = Widget()
        self.screen.add_widget(self.widget_lobby)

        # Create and add GridLayout in Widget
        self.layout = GridLayout(cols=0, rows=2,
                                row_default_height=(self.screen_size[1]/2), 
                                row_force_default=True,
                                orientation='lr-tb')
        self.screen.add_widget(self.layout)
        # breakpoint()
        for i in range(2):
            if i == 0:
                wg_to_add = ButtonToSort(self, text=f"TEST IMG")
            if i == 1:
                wg_to_add = ScrollList()

            self.layout.add_widget(wg_to_add)
        for i in MODES:
            wg_to_add.ids.container.add_widget(ListMenu(self, text=f"{i}"))


    def navegation_ui(self, name_buttons):
        # Create and add Widget in Sceen
        # self.widget_navegation = Widget()
        # self.screen.add_widget(self.widget_navegation)

        # Create and add GridLayout in Widget
        self.layout = GridLayout(cols=5, rows=3, 
                                row_default_height=(self.screen_size[1]/20),
                                row_force_default=True,
                                orientation='lr-bt')
        self.screen.add_widget(self.layout)
        # Insert buttons in layout
        for text in name_buttons.values():
            button_lvl = ButtonToSort(self, text=text)
            self.layout.add_widget(button_lvl)

        # Create and add BoxLayout in Widget
        self.layout = GridLayout(cols=1, rows=1,
                                row_default_height=(self.screen_size[1]/20),
                                row_force_default=True,
                                col_default_width=(self.screen_size[1]/6),
                                col_force_default=True, orientation='tb-lr')
        self.screen.add_widget(self.layout)
        # Insert buttons in layout
        for i in range(1):
            button_lvl = ButtonToSort(self, text=f"Lobby")
            self.layout.add_widget(button_lvl)

    def display_ui(self):
        # Create and add Widget in Sceen
        self.widget_display = Widget()
        label = Label(text=self.logic.get_mode(), text_size=(200, None))
        # self.logic.data['test']['0'][1][1]
        self.widget_display.add_widget(label)
        self.screen.add_widget(self.widget_display)






    def clear_ui(self):
        self.screen.clear_widgets()



if __name__ == "__main__":
    import os
    os.system("python main.py")