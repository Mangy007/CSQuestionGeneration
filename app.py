import json
from random import randint
from core.subject1.chapter2 import k_map
from core.subject1.chapter1 import number_conversion


file = open("config.json")

data = json.load(file)

for i in range(0,data['total_questions']):
    value = randint(1,2) # total number of modules in the subject
    if value==1:
        number_conversion.generate_questions()
    # else:
    #     k_map.minimised_expressions()
    print()