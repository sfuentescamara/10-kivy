from modes import Lenguage, ModePhonetic, ModeGrammar

class SpanishMode(Lenguage):
    """
    <<Concrete Factories>> produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def mode_phonetic(self) -> ModePhonetic:
        return SpanishModePhonetic()
        
    def mode_grammar(self) -> ModeGrammar:
        return SpanishModeGrammar()


class SpanishModePhonetic(ModePhonetic):
    def mode_phonetic(self) -> str:
        return "The result of the spanish phonetic."

class SpanishModeGrammar(ModeGrammar):
    def mode_grammar(self) -> str:
        print("The result of the spanish grammar.")
