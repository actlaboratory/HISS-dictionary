with open("main.csv", "r", encoding="UTF-8") as f:
    lines = f.readlines()

lines = [l.split(",") for l in lines]

for i in range(len(lines)):
    if lines[i][0][0] == "#":
        continue
    lines[i][0] = lines[i][0].translate(str.maketrans(
        {chr(0xFF01 + j): chr(0x21 + j) for j in range(94)}))
    lines[i][0] = lines[i][0].translate(str.maketrans(
        {chr(0x41 + j): chr(0x61 + j) for j in range(26)}))

with open("main.csv", "w", encoding="UTF-8") as f:
    f.writelines([",".join(l) for l in lines])
