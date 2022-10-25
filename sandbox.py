from string import ascii_lowercase


class CeasarDecoder:
    def __init__(self):
        self.output = ''
        self.key = 0
    
    def code_phrase(self, phrase: str, key: int):
        for letter in phrase:
            letter_index = ascii_lowercase.find(letter)
            coded_letter_index = key + letter_index
            output += ascii_lowercase[coded_letter_index]
            return output

    def set_key(self, new_key: int):
        self.key = new_key

    def get_key(self):
        return self.key
    
    def set_output(self, output: str):
        pass
    def decode_phrase(self, phrase: str, key: int):
        self.code_phrase(phrase=phrase, key=-key)


    def get_user_input(self):
        pass
