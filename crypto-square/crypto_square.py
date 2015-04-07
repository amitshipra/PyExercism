__author__ = 'agupt15'

import string
import math


def encode(text):
    if text == '':
        return ''

    cleaned_text = clean(text)
    partition_size = get_partition_size(cleaned_text)
    partitions = [cleaned_text[x:x+partition_size] for x in range(0, len(cleaned_text), partition_size)]

    result = [[partition[idx] for partition in partitions if idx < len(partition)] for idx in range(partition_size)]

    return ' '.join([''.join(element) for element in result])


def clean(text):
    if text is None:
        return ''
    text = text.lower()
    return ''.join([x for x in text if x in string.ascii_lowercase or x in string.digits])


def get_partition_size(clean_txt):
    sqrt = math.sqrt(len(clean_txt))
    if sqrt == int(sqrt):
        print('Perfect Square')
        return int(sqrt)
    else:
        return int(sqrt + 1)