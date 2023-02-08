from Modes import Lenguage, ModePhonetic, ModeGrammar

class EnglishMode(Lenguage):
    """
    <<Concrete Factories>> produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def mode_phonetic(self) -> ModePhonetic:
        return EnglishModePhonetic()
        
    def mode_grammar(self) -> ModeGrammar:
        return EnglishModeGrammar()
        

class EnglishModePhonetic(ModePhonetic):
    def mode_phonetic(self) -> str:
        return "The result of the english phonetic."

class EnglishModeGrammar(ModeGrammar):
    def mode_grammar(self) -> str:
        return "The result of the english grammar."
