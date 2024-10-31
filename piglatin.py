class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase


    def translate(self) -> str:
        if self.phrase == "":
            return "nil"
        return self.phrase

    def vowel(self, word: str):
        self.phrase.lower()
        vowels = "aeiou"
        if word[0] in vowels:
            if word[-1] == "y":
                return word + "nay"
            elif word[-1] in vowels:
                return word + "yay"
            else:
                return word + "ay"
        return word

    def remove_translate(self, word: str):
        self.phrase.lower()
        vowels = "aeiou"
        if word[0] not in vowels:
            return word[1:] + word[0] + "ay"
        return word

    def remove_two_translate(self, word: str):
        self.phrase.lower()
        vowels = "aeiou"
        if (word[0] and word[1]) not in vowels:
            return word[2:] + word[0] + word[1] + "ay"
        return word







