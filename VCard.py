from kivy.properties import StringProperty
from plyer import tts

from OBModo import Modo

class Card(Modo):

    Screen = ""
    title = StringProperty("otro")
    text = StringProperty("Let's Go!")
    text_hiden = StringProperty("")
    bool_show = False
    bool_randomVerbs = False
    index = -1

    
    def back(self):
        self.index -= 1
        if self.index < 0:
            self.index = len(self.data)-1
        self.new(self.index)

    def next(self):
        self.index += 1
        if self.index > len(self.data)-1:
            self.index = 0
        self.new(self.index)

    def randomNext(self):
        id = self.randomize(self.rl_data)
        if(self.bool_randomVerbs):
            self.id_verb = self.randomize(self.rl_data_1)
            self.text = self.data_1[self.id_verb][0]
            self.verb = self.data_1[self.id_verb]
        self.data = self.inst_DictVerb.functionVerb(self.verb)
        if int(id) > 0:
            self.new(id)
        else:
            pass

    def new(self, select):
        self.text_hiden = ""
        self.bool_show = False
        self.form_verb = self.data[str(select)]
        self.title = self.form_verb[0]
        if(not self.bool_randomVerbs):
            self.text = self.form_verb[1]

    def show(self):
        try:
            if self.bool_show == False:
                self.text_hiden = self.form_verb[2]
                self.bool_show = True
            else:
                self.text_hiden = ""
                self.bool_show = False
        except:
            pass

    def readIt(self):
        tts.speak(message=self.text_hiden)