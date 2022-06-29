



from pathlib import Path

path = Path("Question1/Dataset")
lis = []



for p in path.glob("*.csv"):
    lis.append(p)


total = len(lis)

print("------------------------------------------------")
print(f" CSV File Count: {total} files")
print("------------------------------------------------")