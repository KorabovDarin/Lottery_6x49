"""
    This file is to analyze the winning numbers.
"""

import pandas as pd
from collections import Counter, OrderedDict
import pickle

df = pd.read_excel("6x49.xlsx")

numbers = df['Numbers']

list_numbers = []

for num in numbers:
    win_numbers = num.split(",")
    for n in win_numbers:
        list_numbers.append(n)

temp_dict = OrderedDict()

for key, value in zip(Counter(list_numbers).keys(), Counter(list_numbers).values()):
    temp_dict[int(key)]= int(value)

od = OrderedDict(sorted(temp_dict.items()))

with open('dict_numbers.pickle', 'wb') as handle:
    pickle.dump(od, handle, protocol=pickle.HIGHEST_PROTOCOL)