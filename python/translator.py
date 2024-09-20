import sys

class BrailleTranslator:
    BRAILLE_TO_ENGLISH = {
        'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
        'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
        'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
        'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
        'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
        'O..OOO': 'z', '......': ' '
    }

    ENGLISH_TO_BRAILLE = {v: k for k, v in BRAILLE_TO_ENGLISH.items()}

    NUMBER_PREFIX = '.O.O.O'
    CAPITAL_PREFIX = '.....O'

    NUMBERS = {
        'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5',
        'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '0'
    }

    def translate(self, input_string):
        return self.braille_to_english(input_string) if self.is_braille(input_string) else self.english_to_braille(input_string)

    @staticmethod
    def is_braille(input_string):
        return all(char in 'O.' for char in input_string)

    def braille_to_english(self, input_string):
        chars = [input_string[i:i+6] for i in range(0, len(input_string), 6)]
        result = ""
        capitalize_next = False
        number_mode = False

        for char in chars:
            if char == self.CAPITAL_PREFIX:
                capitalize_next = True
            elif char == self.NUMBER_PREFIX:
                number_mode = True
            else:
                letter = self.BRAILLE_TO_ENGLISH.get(char)
                if letter:
                    if number_mode and letter in self.NUMBERS:
                        result += self.NUMBERS[letter]
                    else:
                        result += letter.upper() if capitalize_next else letter
                        number_mode = False
                    capitalize_next = False

        return result

    def english_to_braille(self, input_string):
        result = ""
        for char in input_string:
            if char.isupper():
                result += self.CAPITAL_PREFIX + self.ENGLISH_TO_BRAILLE[char.lower()]
            elif char.isdigit():
                if not result.endswith(self.NUMBER_PREFIX):
                    result += self.NUMBER_PREFIX
                result += self.ENGLISH_TO_BRAILLE[next(k for k, v in self.NUMBERS.items() if v == char)]
            else:
                result += self.ENGLISH_TO_BRAILLE[char.lower()]
        return result

def main():
    if len(sys.argv) < 2:
        print("Please provide a string to translate.")
        sys.exit(1)
    
    input_string = ' '.join(sys.argv[1:])
    translator = BrailleTranslator()
    print(translator.translate(input_string))

if __name__ == "__main__":
    main()
