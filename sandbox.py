from string import ascii_lowercase

class CaesarDecoder:
    def __init__(self):
        self.__output: str = ''
        self.__key: int = 3

    def get_key(self):
        return self.__key
    
    def __set_output(self, output: str):
        self.__output = output
    
    def get_output(self):
        return self.__output
    
    def code_phrase(self, phrase: str, *key: int):
        def letter_cycle(key: int):
            output: str = ""
            for letter in phrase:
                letter_index = ascii_lowercase.find(letter)
                coded_letter_index = letter_index + key
                output += ascii_lowercase[coded_letter_index]
            self.__set_output(output=output)
            return self.get_output()
                
        if key:
            users_key = key[0]
            letter_cycle(users_key)
        else:
            default_key = self.get_key()
            letter_cycle(default_key)
            
    
    def decode_phrase(self, phrase: str, *key: int):
        try:
            self.code_phrase(phrase, key[0])
        except IndexError:
            self.code_phrase(phrase, -self.get_key())
        return self.get_output()
    
a = CaesarDecoder()
print(a.code_phrase(phrase="hello"))
