from modes import json, Lenguage, ModeExpressions, ModeGrammar, ModePhonetic

class EnglishMode(Lenguage):
    """
    <<Concrete Factories>> produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """
    def __init__(self):
        self.properties = {
            'lenguage':"English"
                           }

    def mode_phonetic(self) -> ModePhonetic:
        return EnglishModePhonetic()
        
    def mode_grammar(self) -> ModeGrammar:
        return EnglishModeGrammar()
        
    def mode_expressions(self) -> ModeExpressions:
        return EnglishModeExpresions(prop=self.properties)
        

class EnglishModePhonetic(ModePhonetic):
    def mode_phonetic(self) -> str:
        return "The result of the english phonetic."

class EnglishModeGrammar(ModeGrammar):
    """
    <<Concrete Mode>> 
    
    """
    def __init__(self, debug=True):
        if debug:
            print("Concrete mode grammar initiated")
        if not self.read_data():
            raise("Data not readed!")
        
    def __del__(self, debug=True):
        if debug:
            print("Concrete mode grammar deleted")

    def read_data(self) -> bool:
        # with open("verbs.json") as verb_file:
        #     self.verbs = json.load(verb_file)

        return True

class EnglishModeExpresions(ModeExpressions):
    """
    <<Concrete Mode>> 
    
    """
    def __init__(self, prop, debug=True):

        super(EnglishModeExpresions, self).__init__()

        self.prop = prop
        if debug:
            print("Concrete mode expressions initiated")
        if not self.read_data("expressions.json"):
            raise("Data not readed!")
    