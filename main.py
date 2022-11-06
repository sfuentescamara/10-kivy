from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from random import seed, random, randint

import json
# 

class Modo(Screen):
    Screen = StringProperty("Lobby")

    def changeScreen(where):
        pass

class Lobby(Modo):
    Screen = "Lobby"

class Grammar(Modo):
    Screen = "Grammar"
    title = StringProperty("HOME")
    text = StringProperty("Let's Go!")
    text_hiden = StringProperty("")
    index = -1
    bool_show = False
    title_randomVerbs = StringProperty("Activate Randoms Verbs")
    bool_randomVerbs = False
    allFormsVerbs = {}

    verb = ["juego", "play", "played", "played", "playing"]

    with open("verbs.json") as verb_file:
        allVerbs = json.load(verb_file)

    class DictVerb():
        def functionVerb(self, verb):
            self.allFormsVerbs = {0   :["Present Simple"                    ,"Juego"                          ,f"I {verb[1]}"],
                    1   :["Present Continuous"                ,"Estoy jugando"                  ,f"I'm {verb[4]}"],
                    2   :["Present Perfect Simple"            ,"He jugado"                      ,f"I've {verb[3]}"],
                    3   :["Present Perfect Continuous"        ,"He estado jugando"              ,f"I've been {verb[4]}"],
                    4   :["Past Simple"                       ,"Jugé"                           ,f"I {verb[2]}"],
                    5   :["Past Continuous"                   ,"Estaba jugando"                 ,f"I was {verb[4]}"],
                    6   :["Past Perfect Simple"               ,"Había jugado"                   ,f"I had {verb[3]}"],
                    7   :["Past Perfect Continuous"           ,"Había estado jugando"           ,f"I had been {verb[4]}"],
                    8   :["Future Simple"                     ,"Jugaré"                         ,f"I will {verb[1]}"],
                    9   :["Future Continuous"                 ,"Estaré jugando"                 ,f"I will be {verb[4]}"],
                    10  :["Future Perfect Simple"             ,"Habré jugado"                   ,f"I will have {verb[3]}"],
                    11  :["Future Perfect Continuous"         ,"Habré estado jugando"           ,f"I will have been {verb[4]}"],
                    12  :["Be Going To Simple"                ,"Voy a jugar"                    ,f"I'm going to {verb[1]}"],
                    13  :["Be Going To Continuous"            ,"Voy a estar jugando"            ,f"I'm going to be {verb[4]}"],
                    14  :["Future Past/Desire Simple"         ,"Jugaría"                        ,f"I would {verb[1]}"],
                    15  :["Future Past Perf/Desire Simple"    ,"Habría jugado"                  ,f"I would have {verb[3]}"],
                    16  :["Future Past Perf/Desire Continuous","Habría estado jugando"          ,f"I would have been {verb[4]}"],
                    17  :["Modal verb High obligation"        ,"Debo jugar"                     ,f"I must {verb[1]}"],
                    18  :["Modal verb Med. obligation"        ,"Tengo que jugar"                ,f"I have/need to {verb[1]}"],
                    19  :["Modal verb Low obligation"         ,"Debería jugar"                  ,f"I should {verb[1]}"],
                    20  :["Modal verb Low Past obligation"    ,"Debería haber jugado"           ,f"I should have {verb[3]}"],
                    21  :["High probability"                  ,"Puedo jugar"                    ,f"I may {verb[1]}"],
                    22  :["Low probability"                   ,"Podría jugar"                   ,f"I might {verb[1]}"],
                    23  :["First Condicional *If*"            ,"Posibles situaciones futuras"   ,f"If I play, I will improve"],
                    24  :["First Condicional *Even if*"       ,"Posibles situaciones futuras"   ,f"Even if I play, I won't improve"],
                    # 25  :["Second Condicional *If*"           ,"Posibles situaciones futuras"   ,f"If I {verb[1]}, I will improve"],
                    # 26  :["Second Condicional *Even if*"      ,"Posibles situaciones futuras"   ,f"Even if I {verb[1]}, I won't improve"],
                    }
            return self.allFormsVerbs

    allFormsVerbs = DictVerb().functionVerb(verb)
    rl_verbs = [x for x in allVerbs]
    rl_formsVerbs = [x for x in allFormsVerbs]

    def randomize(self, x):
        if len(x) != 0:
            random = randint(0, len(x)-1)
            for i, item in enumerate(x):
              if i == random:
                    # rl_verbs.pop(item)
                    x.pop(i)
                    return item
        else:
            self.title = "NICE JOB!"
            self.text = ""
            self.text_hiden = ""
            self.rl_formsVerbs = [x for x in self.allFormsVerbs]
            self.rl_verbs = [x for x in self.allVerbs]

        return -1

    def back(self):
        self.index -= 1
        if self.index < 0:
            self.index = len(self.allFormsVerbs)-1
        self.new(self.index)

    def next(self):
        self.index += 1
        if self.index > len(self.allFormsVerbs)-1:
            self.index = 0
        self.new(self.index)

    def randomNext(self):
        id = self.randomize(self.rl_formsVerbs)
        if(self.bool_randomVerbs):
            self.id_verb = self.randomize(self.rl_verbs)
            self.text = self.allVerbs[self.id_verb][0]
            self.verb = self.allVerbs[self.id_verb]
        self.allFormsVerbs = self.DictVerb().functionVerb(self.verb)
        if id > 0:
            self.new(id)
        else:
            pass

    def new(self, select):
        self.text_hiden = ""
        self.bool_show = False
        self.form_verb = self.allFormsVerbs[select]
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

    def reset(self):
        self.title = "HOME"
        self.text = "Let's Go!"
        self.text_hiden = ""
        self.form_verb = ""
        self.index = -1
        self.bool_show = False
        self.bool_randomVerbs = False
        self.title_randomVerbs = "Activate Random Verbs"
        self.verb = ["juego", "play", "played", "played", "playing"]
        self.rl_formsVerbs = [x for x in self.allFormsVerbs]
        self.rl_verbs = [x for x in self.allVerbs]

    def randomVerbs(self):
        if self.bool_randomVerbs == False:
            self.bool_randomVerbs = True
            self.title_randomVerbs = "Desactivate Random Verbs"
        else:
            self.bool_randomVerbs = False
            self.title_randomVerbs = "Activate Random Verbs"
            self.verb = ["juego", "play", "played", "played", "playing"]




class Vocabulary(Modo):
    Screen = "Vocabulary"

class WindowMain(ScreenManager):
    title = "WindowMain"
    text = StringProperty("Let's Go!")
    text_hiden = StringProperty("")
    index = -1
    bool_show = False

sm = ScreenManager()
sm.add_widget(Lobby(name="Lobby"))
sm.add_widget(Grammar(name="Grammar"))
sm.add_widget(Vocabulary(name="Vocabulary"))

class Aplication(MDApp):
    def build(self):
        kv = Builder.load_file("display.kv")
        
        return kv


if __name__ == "__main__":
    randomApp = Aplication()
    randomApp.run()