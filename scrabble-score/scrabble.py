__author__ = 'agupt15'

SCORE_CARD = {'AEIOULNRST': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10}


def score(word):
    word = word.strip().upper()
    if word == '':
        return 0
    return sum([SCORE_CARD[key] for key, value in SCORE_CARD.items() for ch in word if ch in key])


