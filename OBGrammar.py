
from kivy.properties import StringProperty
from plyer import tts

from OBModo import Modo
from VCard import Card

import json
from random import seed, random, randint

class Grammar(Card):
    
    Screen = "Grammar"
    title = StringProperty("Home")
    text = StringProperty("Let's Go!")
    text_hiden = StringProperty("")
    title_randomVerbs = StringProperty("Activate Random Verbs")
    bool_show = False
    bool_randomVerbs = False
    index = -1
    data = {}
    verb = ["juego", "play", "played", "played", "playing"]
    data_1 = None
    rl_data_1 = None
    rl_data = None
    inst_DictVerb = None

    def __init__(self, **kwargs):
        super(Grammar, self).__init__(**kwargs)

        with open("verbs.json") as verb_file:
            self.data_1 = json.load(verb_file)

        class DictVerb():
            def functionVerb(self, verb):
                
                self.data = {"0"   :["Present Simple"                    ,"Juego"                          ,f"I {verb[1]}"],
                        "1"   :["Present Continuous"                ,"Estoy jugando"                  ,f"I'm {verb[4]}"],
                        "2"   :["Present Perfect Simple"            ,"He jugado"                      ,f"I've {verb[3]}"],
                        "3"   :["Present Perfect Continuous"        ,"He estado jugando"              ,f"I've been {verb[4]}"],
                        "4"   :["Past Simple"                       ,"Jugé"                           ,f"I {verb[2]}"],
                        "5"   :["Past Continuous"                   ,"Estaba jugando"                 ,f"I was {verb[4]}"],
                        "6"   :["Past Perfect Simple"               ,"Había jugado"                   ,f"I had {verb[3]}"],
                        "7"   :["Past Perfect Continuous"           ,"Había estado jugando"           ,f"I had been {verb[4]}"],
                        "8"   :["Future Simple"                     ,"Jugaré"                         ,f"I will {verb[1]}"],
                        "9"   :["Future Continuous"                 ,"Estaré jugando"                 ,f"I will be {verb[4]}"],
                        "10"  :["Future Perfect Simple"             ,"Habré jugado"                   ,f"I will have {verb[3]}"],
                        "11"  :["Future Perfect Continuous"         ,"Habré estado jugando"           ,f"I will have been {verb[4]}"],
                        "12"  :["Be Going To Simple"                ,"Voy a jugar"                    ,f"I'm going to {verb[1]}"],
                        "13"  :["Be Going To Continuous"            ,"Voy a estar jugando"            ,f"I'm going to be {verb[4]}"],
                        "14"  :["Future Past/Desire Simple"         ,"Jugaría"                        ,f"I would {verb[1]}"],
                        "15"  :["Future Past Perf/Desire Simple"    ,"Habría jugado"                  ,f"I would have {verb[3]}"],
                        "16"  :["Future Past Perf/Desire Continuous","Habría estado jugando"          ,f"I would have been {verb[4]}"],
                        "17"  :["Modal verb High obligation"        ,"Debo jugar"                     ,f"I must {verb[1]}"],
                        "18"  :["Modal verb Med. obligation"        ,"Tengo que jugar"                ,f"I have/need to {verb[1]}"],
                        "19"  :["Modal verb Low obligation"         ,"Debería jugar"                  ,f"I should {verb[1]}"],
                        "20"  :["Modal verb Low Past obligation"    ,"Debería haber jugado"           ,f"I should have {verb[3]}"],
                        "21"  :["High probability"                  ,"Puedo jugar"                    ,f"I may {verb[1]}"],
                        "22"  :["Low probability"                   ,"Podría jugar"                   ,f"I might {verb[1]}"],
                        "23"  :["First Condicional *If*"            ,"Posibles situaciones futuras"   ,f"If I play, I will improve"],
                        "24"  :["First Condicional *Even if*"       ,"Posibles situaciones futuras"   ,f"Even if I play, I won't improve"],
                        "25"  :["Second Condicional *If*"          ,"Accion muy improvable"           ,f"If I {verb[2]}, I would improve"],
                        "26"  :["Second Condicional *Even if*"     ,"Accion muy improvable"           ,f"Even if I {verb[2]}, I wouldn't improve"],
                        "27"  :["Third Condicional *If*"           ,"Accion pasada muy improvable"   ,f"If I had {verb[3]}, I would improve"],
                        "28"  :["Third Condicional *Even if*"      ,"Accion pasada muy improvable"   ,f"Even if I had {verb[3]}, I wouldn't improve"]
                        }
                return self.data

        
        self.inst_DictVerb = DictVerb()
        self.data = DictVerb().functionVerb(self.verb)
        self.rl_data_1 = [x for x in self.data_1]
        self.rl_data = [x for x in self.data]

    def randomize(self, x):
        if len(x) != 0:
            random = randint(0, len(x)-1)
            for i, item in enumerate(x):
              if i == random:
                    # rl_data_1.pop(item)
                    x.pop(i)
                    return item
        else:
            self.title = "NICE JOB!"
            self.text = ""
            self.text_hiden = ""
            self.rl_data = [x for x in self.data]
            self.rl_data_1 = [x for x in self.data_1]

        return -1

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
        self.rl_data = [x for x in self.data]
        self.rl_data_1 = [x for x in self.data_1]

    def randomVerbs(self):
        if self.bool_randomVerbs == False:
            self.bool_randomVerbs = True
            self.title_randomVerbs = "Desactivate Random Verbs"
        else:
            self.bool_randomVerbs = False
            self.title_randomVerbs = "Activate Random Verbs"
            self.verb = ["juego", "play", "played", "played", "playing"]

