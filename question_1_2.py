import csv
from pathlib import Path
import pandas
import json

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

    # if need to save bytes, run this
    # json = csv.to_json(r"Question1\Dataset" + f"\{file_name[0]}.json", indent=4, orient="index")
    
    new_json = csv.to_json(orient="index")
    with open(r"Question1\Dataset" + f"\{file_name[0]}.json", 'w', encoding='utf-8') as jsonf: 
        parsed = json.loads(new_json)
        jsonString = json.dumps(parsed, indent=4)
        jsonf.write(jsonString)

