from kivy.properties import StringProperty
from plyer import tts
from kivy.uix.spinner import Spinner

from VCard import Card

import json

class Vocabulary(Card):
    Screen = "Vocabulary"
    
    title = StringProperty("---")
    text = StringProperty("Let's Go!")
    text_hiden = StringProperty("---")
    bool_show = False
    bool_randomVerbs = False
    index = -1
    data = {}
    
    with open("vocabulary.json", encoding='utf-8', errors='ignore') as file:
        vocabulary = json.load(file)
        
    select_list = [x for x in vocabulary.keys()]
    select_list.append('Add')

    spinner = Spinner(
        values=(select_list),
        size_hint=(None, None),
        size=(100, 0.9))

    def spinner_selection(self, spinner, text):
        print('The spinner', spinner, 'has text', text)
        
        if text == 'List':
            pass
        elif text == 'Add':
            pass
        else:
            self.data = self.vocabulary[text]
            print(self.data)
        pass

    def start(self):
        print("DOO")
        
    
        self.spinner.bind(text=self.spinner_selection)
       
        # TODO: Create a file to save expressions
        # TODO: Randomice and print expressions in spanish
        # TODO: Read the expressions