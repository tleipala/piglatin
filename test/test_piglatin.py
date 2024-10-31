import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_something(self):
        pass

    #story 1

    def test_translator_with_phrase(self):
        translator = PigLatin("hello world")
        print(translator)

    def test_translator_get_phrase(self):
        translator = PigLatin("Latin")
        phrase = translator.get_phrase()
        print(phrase)

    #story 2

    def test_translator_empty_phrase(self):
        translator = PigLatin("")
        translation = translator.translate()
        print(translation)

    #story 3

    def test_translator_vowel(self):
        translator = PigLatin("Latin")
        phrase = translator.vowel("latin")
        print(phrase)

    #story 4

    def test_translator_piglatin(self):
        translator = PigLatin("hello")
        phrase = translator.remove_translate("hello")
        print(phrase)

    #story 5

    def test_translator_piglatin_two(self):
        translator = PigLatin("know")
        phrase = translator.remove_two_translate("know")
        print(phrase)























