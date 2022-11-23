from kivymd.uix.list import MDList, OneLineListItem
from kivy.properties import StringProperty
from kivy.uix.spinner import Spinner

from OBModo import Modo
from VCard import Card

import json

# Info:
# About Fhrasal verbs: https://elblogdeidiomas.es/150-phrasalverbs-traduccion-ejemplo/

class Expressions(Card):
    Screen = "Expressions"
    title = StringProperty("Home")
    text = StringProperty("Let's Go!")
    text_hiden = StringProperty("")
    bool_show = False
    bool_randomVerbs = False
    index = -1
    data = {}

    with open("expressions.json") as file:
        expressions = json.load(file)

    expressions_list = [x for x in expressions.keys()]
    expressions_list.append('Add')
    spinner = Spinner(
        # default value shown
        text='Home',
        # available values
        values=(expressions_list),
        size_hint=(None, None),
        size=(100, 0.9))
    
    def spinner_selection(self, spinner, text):
        print('The spinner', spinner, 'has text', text)
        
        if text == 'Expresions':
            pass
        elif text == 'Add':
            pass
        else:
            self.data = self.expressions[text]
            print(self.data)
        pass

    def start(self):
        print("DOO")
        
        self.spinner.bind(text=self.spinner_selection)
       
        # TODO: Create a file to save expressions
        # TODO: Randomice and print expressions in spanish
        # TODO: Read the expressions