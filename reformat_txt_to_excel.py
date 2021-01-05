"""
    This script is used to convert the txt file to an Excel sheet
    and a csv file.
"""

import pandas as pd

years_list = []
id_list = []
numbers_list = []

with open("toto_6x49.txt") as f:
    for f in f.readlines():
        f = f.strip('\n').strip()
        year = f.split(",")[0]
        id = f.split(",")[1]
        winning_numbers = ",".join(f.split(",")[2:])
        years_list.append(year)
        id_list.append(id)
        numbers_list.append(winning_numbers)

out_dict = {
    "Year":years_list,
    "ID":id_list,
    "Numbers":numbers_list
}
df = pd.DataFrame.from_dict(out_dict)
df.to_excel("6x49.xlsx", index=False)
df.to_csv("6x49.csv", index=False)
