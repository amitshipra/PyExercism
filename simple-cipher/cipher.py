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
        self.all_letters = string.ascii_lowercase
        self._key_map = key

    def encode(self, plain_text):
        return ''.join(self.encode_decode(plain_text, encode=True))

    def decode(self, cryptic):
        return ''.join(self.encode_decode(cryptic, encode=False))

    def encode_decode(self, text, encode=True):
        result = []
        for i, ch in enumerate(text):
            _original_idx = self.all_letters.index(ch)
            if i < len(self._key_map) - 1:
                _code = self._key_map[i]
            else:
                _code = 'a'
            _code_idx = self.all_letters.index(_code)
            if encode is False:
                _idx = _original_idx - _code_idx
            else:
                _idx = _original_idx + _code_idx

            if _idx > 25:
                _idx -= 26
            result.append(self.all_letters[_idx])
        return result
