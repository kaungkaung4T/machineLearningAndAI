



import csv
from pathlib import Path
import pandas


path = Path("Question1/Dataset")

    

def convert_row(row):
    return """
    <object>
        <tag>%s</tag>
        <bndbox>
            <x>%s</x>
            <y>%s</y>
            <width>%s</width>
            <height>%s</height>
        </bndbox>
    </object>""" % (row[4], row[0], row[1], row[2], row[3])


for p in path.glob("*.csv"):
    data = []
    file = open(p)
    read_csv = csv.reader(file)
    for row in read_csv:
        data.append(row)

    new_path = str(p)
    new_path = new_path.split("\\")
    file_name = str(new_path[2])
    file_name = file_name.split(".")

    # print ('\n'.join([convert_row(row) for row in data]))
    with open(f'Question1/Dataset/{file_name[0]}.xml', 'w') as file: 
        file.write("""<annotation>""" + "".join([convert_row(row) for row in data]) + "\n" + """</annotation>""")

file.close()