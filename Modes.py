from __future__ import annotations
from abc import ABC, abstractmethod

import json

class Lenguage(ABC):
    """
    <<The Abstract Factory>> interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """
    @abstractmethod
    def mode_phonetic(self) -> ModePhonetic:
        pass

    @abstractmethod
    def mode_grammar(self) -> ModeGrammar:
        pass

    # @abstractmethod
    # def mode_vocabulary(self) -> AbstractModeVocabulary:
    #     pass
    
    @abstractmethod
    def mode_expressions(self) -> ModeExpressions:
        pass

########################################################

class Mode:
    """
    
    """
    def get_mode(self) -> str:
        return self.mode_name

    def read_data(self, file) -> bool:
        
        try:
            with open(file) as data_file:
                self.data = json.load(data_file)
        
        except Exception as error:
            print("ERROR: Reding data!")
            return False
        
        if not bool(self.data):
            return False
        else:
            return True

########################################################

class ModePhonetic(Mode):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """
    def read_data(self, file) -> bool:
        return super(ModePhonetic, self).read_data(file)

class ModeGrammar(Mode):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """
    def read_data(self, file) -> bool:
        return super(ModeGrammar, self).read_data(file)

class ModeExpressions(Mode):
    """
    << Abstract product >>
    """

    def __init__(self) -> None:

        self.mode_name = "Expressions"

        super(ModeExpressions, self).__init__()

########################################################


