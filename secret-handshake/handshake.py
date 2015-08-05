__author__ = 'dias'

##
# This is not COMPLETE yet. Many boundary conditions remain.
# Specifically - reverse in codes[] need to be tackled.
# 0 needs to be returned for unidentified codes. etc etc
# Take a hard look whenever you have time.
##

SIGNALS = {1: 'wink', 10: 'double blink', 100: 'close your eyes', 1000: 'jump', 10000: 'reverse'}


def handshake(decimal):
    if decimal <= 0:
        return []

    binary = to_binary(decimal)
    print(binary)
    length = len(binary)
    codes = [SIGNALS[n * pow(10, length - i - 1)] for i, n in enumerate(binary) if
             n * pow(10, length - i - 1) in SIGNALS]

    if 'reverse' in codes:
        codes.remove('reverse')
        codes = codes[::-1]

    return codes[::-1]


def to_binary(num):
    if isinstance(num, str) and valid_binary(num):
        return [int(x) for x in num]

    binary = list()
    while num > 0:
        binary.append(num % 2)
        num /= 2
    return binary[::-1]


def valid_binary(str_num):
    for x in str_num:
        if x != '0' and x != '1':
            return False
    if len(str_num) == 0:
        return False
    return True


def code(signals):
    binary = int()

    def getKey(value):
        for k, v in SIGNALS.items():
            if v == value:
                return k
        return None

    for signal in signals:
        binary += getKey(signal)

    return binary


print(code(['jump','double blink']))
print(handshake('11011'))
