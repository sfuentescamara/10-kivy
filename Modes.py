from __future__ import annotations
from abc import ABC, abstractmethod


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
    # def create_mode_vocabulary(self) -> AbstractModeVocabulary:
    #     pass
    
    # @abstractmethod
    # def create_mode_expression(self) -> AbstractModeExpression:
    #     pass

########################################################

class Mode(ABC):
    def read_data(self) -> str:
        pass

########################################################

class ModePhonetic(Mode):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    def read_data(self) -> str:
        pass

class ModeGrammar(Mode):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """
    def read_data(self) -> str:
        print("BASE STADARD FUNCTIONS LOADed")
        pass

########################################################


