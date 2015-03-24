__author__ = 'agupt15'


class Allergies:
    def __init__(self, num):
        ALLERGY_MAP = [(1, 'eggs'), (2, 'peanuts'), (4, 'shellfish'), (8, 'strawberries'), (16, 'tomatoes'),
                       (32, 'chocolate'), (64, 'pollen'), (128, 'cats')]
        self.num_allergies = num
        self.allergies = list()

        for score, name in ALLERGY_MAP:
            print(score, name)

    def is_allergic_to(self, allergy):
        return allergy in self.allergies

    def list(self):
        return self.allergies


print(Allergies(5).list())