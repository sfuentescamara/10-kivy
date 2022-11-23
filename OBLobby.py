from OBModo import Modo
from OBGrammar import Grammar
from OBExpressions import Expressions
from OBVocabulary import Vocabulary

class Lobby(Modo):
    Screen = "Lobby"

    def changeScreen(self, w_start):
        eval(w_start)().start()