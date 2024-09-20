# Python Instructions

Note that the Python version used is 3.8

# Braille Translator

This project implements a command-line Braille translator that can convert text between English and Braille. It supports translation in both directions and handles uppercase letters, numbers, and spaces.

## Features

- Translate English text to Braille
- Translate Braille to English text
- Support for uppercase letters
- Support for numbers
- Automatic detection of input type (English or Braille)

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/braille-translator.git
   cd braille-translator
   ```

2. No additional dependencies are required.

## Usage

To use the Braille translator, run the `translator.py` script with your input text as command-line arguments:

```
python3 translator.py <input text>
```

For example:

```
python3 translator.py Hello World
```

This will output the Braille translation:

```
.....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
```

To translate from Braille to English, simply input the Braille code:

```
python3 translator.py .....OO.OO..O..O..O.O.O.O.O.O.O..OO........OOO.OO..OO.O.OOO.O.O.O.OO.O..
```

This will output:

```
Hello World
```

## Testing

To run the unit tests, use the following command:

```
python3 test_translator.py
```

This will run the test suite and report any failures.

## Implementation Details

The Braille translator is implemented in the `BrailleTranslator` class in `translator.py`. It uses dictionaries to map between English characters and their Braille representations. The translator can handle:

- Lowercase letters (a-z)
- Uppercase letters (A-Z)
- Numbers (0-9)
- Spaces

For Braille input, each character is represented by a 6-character string of dots (O) and dashes (.).

## Limitations

- The current implementation does not support punctuation marks.
- It assumes well-formed input and may not handle all edge cases.

## Future Improvements

- Add support for punctuation marks
- Implement error handling for malformed input
- Extend the test suite to cover more cases
