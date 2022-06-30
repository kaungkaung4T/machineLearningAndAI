import csv
from pathlib import Path
import pandas


path = Path("Question1/Dataset")
index_num = 0
num = 0


for p in path.glob("*.csv"):
    num = 0
    index_num = 0
    columns = ["x", "y", "width", "height", "tag"]
    
    csv = pandas.read_csv(p, names=columns, sep=",")


    while num < len(csv):
        num += 1
        if num >= 10:
            csv.rename(index={index_num:"record_"+str(num)}, inplace=True)
        else:
            csv.rename(index={index_num:"record_0"+str(num)}, inplace=True)
        index_num += 1

    
    # x, y, width, height, tag are float and string. Also tested with type and can also test like this,
    # print(type(csv.tag.iloc[0]))

    new_path = str(p)
    new_path = new_path.split("\\")
    file_name = str(new_path[2])
    file_name = file_name.split(".")

    csv.to_json(r"C:\Users\KaungKaung\Desktop\gw\gw_test\Question1\Dataset" + f"\{file_name[0]}.json", indent=4, orient="index")

