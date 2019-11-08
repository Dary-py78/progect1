
import random
"""
We need to deliver a lot of coal from a mine
The best way is to use 'pony' for this work

So, we are going to get about 100000 ph of coal.


The task is:
How expensive it will be?

1 - pony - 100 lbs for 1 hour
2 - 1 pony need 20 lbs of food a week
3 - 1 lbs of food costs ?
4 - for each pony we have additional cost for medical assistance"""

horse_names = ["Pokey", "Bullseye", "Pericles", "Arrow", "Shabas", "Anna Bell", "Baymont", "Rainstorm", "Midnight",
               "Bolaro", "Flurry", "Chino", "Wild", "Sparkle", "Thunderflame", "Hawkins", "Maisie", "Night", "Stallion",
               "Blaze",
               ]
class Horse:
    MIN_AGE = 1
    MAX_AGE = 16
    GENDERS=  ["MMMMM", "FFFFF"]
    available_breeds = ["Frisian", "Akhal-Teke", "Arab", "Hanover", "Iberian"]
    coat_colours = ["black", "bay", "red", "gray"]

    def __init__(self, name, age, gender, breed, coat_colour):
        self.name = name
        self.age = age
        self.breed = breed
        self.gender = gender
        self.coat_colour = coat_colour

    def __str__(self):
        return f"{self.name}, {self.age}, {self.breed}, {self.gender}, {self.coat_colour}"

class Costs (Horse):

    def __init__(self, name,age, gender, coat_colour, how_many_ph_order):
        super().__init__(self, name, age, gender, coat_colour)
        self.how_many_ph_order = how_many_ph_order

    def count_price_for_ponny_service(self):
        ph_for_one_hour = 100
        ibs_of_food_week = 20
        one_kilo_food = 15
        cost_pills_for_pony_for_day = 5
        days_spnt_for_taking_1000ph = (self.how_many_ph_order /ph_for_one_hour)* 0.0417
        for_food_per_day = ibs_of_food_week / 7
        all_costs_for_ponny = (for_food_per_day + one_kilo_food + cost_pills_for_pony_for_day)*days_spnt_for_taking_1000ph
        print("For order number 1 with '{}' ph the final price will be '{}'paunds".format(self.how_many_ph_order,all_costs_for_ponny))
        return all_costs_for_ponny





"""def random_element(some_list):
    return some_list[randint(0, len(some_list)-1)]"""


if __name__ == '__main__':
    b = Costs(name=random.choice(horse_names),
                      age= random.choice([6,1,3,7,9,11,5,4,1]),
                      gender=random.choice(Horse.GENDERS),
                      coat_colour=random.choice(Horse.coat_colours),
                      how_many_ph_order = 100000
                      )
    b.count_price_for_ponny_service()
