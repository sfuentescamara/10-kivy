from Modes import Lenguage
from EnglishFactory import EnglishModePhonetic, EnglishModeGrammar
from SpanishFactory import SpanishModePhonetic, SpanishModeGrammar


class UseModes():
    """
    <<Single factory>> pattern  describes a class that has one creation
    method with a large conditional that based on method parameters
    chooses which product class to instantiate and then return.

    To used it need instance first and later use method:
    a = UseModes(1)
    option = a.select_mode()
    """
    def __init__(self, option: str):
        self.option = option
        # self.create_lobby()

    def create_lobby(self):
        pass

    def select_mode(self):
        if self.option == 1:
            print("Instant SpanishModeGrammar")
            return SpanishModeGrammar()
        if self.option == 2:
            print("Instant EnglishModePhonetic")
            return EnglishModePhonetic()

def client_code(factory: Lenguage) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.mode_grammar()
    # product_b = factory.mode_grammar()

    print(f"{product_a}")
    # print(f"{product_b.mode_grammar(product_a)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the Phonetic factory type:")
    a = UseModes(1)
    option = a.select_mode()
    print(dir(option))
    client_code(option)

    print("\n")

    print("Client: Testing the same client code with the Grammar factory type:")
    # client_code(EnglishModePhonetic())