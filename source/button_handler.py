from config import MODES
from source.modes import Lenguage
from spanish_factory import SpanishMode
from english_factory import EnglishMode

LENGUAGE = 'En'

def button_handler(button: object, gui: object):
    """
    Mode 0: Grammar
    Mode 1: Expressions
    ...
    
    """
    if button.text in MODES:
        
        # Clean ui
        gui.clear_ui()

        # Load logic 
        if LENGUAGE == 'Es':
            if button.text == MODES[0]:
                print("Es-Grammar")
                SpanishMode().mode_grammar()

        if LENGUAGE == 'En':
            if button.text == MODES[0]:
                print("En-Grammar")
                gui.logic = EnglishMode().mode_grammar()
                
            if button.text == MODES[1]:
                print("En-Expressions")
                gui.logic = EnglishMode().mode_expressions()

        #TODO: more logic...

        # Load ui
        name_buttons = {0: "1", 1:"2", 2:"3", 3:"4", 4:"5",
                        5:"<-", 7:" ", 8:"R", 9:" ", 10:"->",
                        11:"Random", 12:" ", 13:"Show", 14:" ", 15:"Play"}
        
        gui.navegation_ui(name_buttons)
        gui.display_ui()

        #TODO: more ui...

    if button.text == "Lobby":
        gui.clear_ui()
        gui.lobby_ui()
        gui.logic = object()
        #TODO: Clean MODE data...


# get_root_window
# remove_widget

# clear_widgets
