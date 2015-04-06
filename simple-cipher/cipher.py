__author__ = 'agupt15'

import string


class Caesar:
    def __init__(self):
        self.all_letters = string.ascii_lowercase

    def get_cipher(self, ch):
        ch = ch.lower()
        if ch == ' ' or ch not in self.all_letters:
            return ''
        idx = self.all_letters.index(ch) + 3
        if idx > len(self.all_letters):
            idx = - 25
        return self.all_letters[idx]

    def get_plain(self, ch):
        ch = ch.lower()
        idx = self.all_letters.index(ch) - 3
        return self.all_letters[idx]

    def encode(self, plain_text):
        return ''.join([self.get_cipher(x) for x in plain_text])

    def decode(self, cryptic):
        return ''.join([self.get_plain(x) for x in cryptic])


class Cipher:
    def __init__(self, key=''):
        self._key = key

    def encode(self, plain_text):
        return None

    def decode(self, cryptic):
        return None


print(Caesar().decode('yhqlylglylfl'))