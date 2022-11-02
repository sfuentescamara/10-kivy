from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from random import seed, random, randint


class Primera(Screen):
  title = StringProperty("HOME")
  text = StringProperty("Let's Go!")
  text_hiden = StringProperty("")
  index = -1
  bool_show = False


  allVerbs = {"sugerir"   :["arise",    "arose",        "arisen"],
                  "ser"       :["be",       "was/were",     "been"  ], 
                  "golpear"   :["beat",     "beat",         "beaten"  ], 

                  }

  allFormsVerbs = {0   :["Present Simple"                    ,"Juego"                          ,"I play"],
                   1   :["Present Continuous"                ,"Estoy jugando"                  ,"I'm playing"],
                   2   :["Present Perfect Simple"            ,"He jugado"                      ,"I've played"],
                   3   :["Present Perfect Continuous"        ,"He estado jugando"               ,"I've been playing"],
                   4   :["Past Simple"                       ,"Jugé"                           ,"I played"],
                   5   :["Past Continuous"                   ,"Estaba jugando"                 ,"I was playing"],
                   6   :["Past Perfect Simple"               ,"Había jugado"                   ,"I had played"],
                   7   :["Past Perfect Continuous"           ,"Había estado jugando"            ,"I had been playing"],
                   8   :["Future Simple"                     ,"Jugaré"                         ,"I will play"],
                   9   :["Future Continuous"                 ,"Estaré jugando"                 ,"I will be playing"],
                   10  :["Future Perfect Simple"             ,"Habré jugado"                   ,"I will have played"],
                   11  :["Future Perfect Continuous"         ,"Habré estado jugando"            ,"I will have been playing"],
                   12  :["Be Going To Simple"                ,"Voy a jugar"                    ,"I'm going to play"],
                   13  :["Be Going To Continuous"            ,"Voy a estar jugando"            ,"I'm going to be playing"],
                   14  :["Future Past/Desire Simple"         ,"Jugaría"                        ,"I would play"],
                   15  :["Future Past Perf/Desire Simple"    ,"Habría jugado"                  ,"I would have played"],
                   16  :["Future Past Perf/Desire Continuous","Habría estado jugando"          ,"I would have been playing"],
                   17  :["Modal verb High obligation"        ,"Debo jugar"                     ,"I must play"],
                   18  :["Modal verb Med. obligation"        ,"Tengo que jugar"                ,"I have/need to play"],
                   19  :["Modal verb Low obligation"         ,"Debería jugar"                  ,"I should play"],
                   20  :["Modal verb Low Past obligation"    ,"Debería haber jugado"           ,"I should have played"],
                   21  :["High probability"                  ,"Puedo jugar"                    ,"I may play"],
                   22  :["Low probability"                   ,"Podría jugar"                   ,"I might play"],
                   23  :["First Condicional"                 ,"",                              ,"If I play, I will improve \n\
                                                                                                 If + subj. + present simple, \
                                                                                                 subj. + will + infinitive"],
                        }

  # rl_verbs = [x for x in allVerbs]
  rl_formsVerbs = [x for x in allFormsVerbs]

  def randomize(self, x):
    if len(x) != 0:
      random = randint(0, len(x)-1)
      for i, item in enumerate(x):
        if i == random:
          # rl_verbs.pop(item)
          self.rl_formsVerbs.pop(i)
          return item
    else:
      self.title = "NICE JOB!"
      self.text = ""
      self.text_hiden = ""
      self.rl_formsVerbs = [x for x in self.allFormsVerbs]

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
    """
        self.verb         set random verb and return a list
        self.form_verb    set random from verbal and return ...
    """
    # self.verb = self.allVerbs[self.randomize(self.rl_verbs)]
    id = self.randomize(self.rl_formsVerbs)
    if id > 0:
      self.new(id)
    else:
      pass

  def new(self, select):
    self.text_hiden = ""
    self.bool_show = False
    self.form_verb = self.allFormsVerbs[select]
    self.title = self.form_verb[0]
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
    # self.rl_verbs = [x for x in allVerbs]
    self.rl_formsVerbs = [x for x in self.allFormsVerbs]

  def randomVerbs(self):
    
    bool_randomVerbs = True


sm = ScreenManager()
sm.add_widget(Primera(name="1"))

class Aplication(MDApp):
  def build(self):
    kv = Builder.load_file("new_window.kv")
    seed()
    
    return kv


if __name__ == "__main__":
  randomApp = Aplication()
  randomApp.run()