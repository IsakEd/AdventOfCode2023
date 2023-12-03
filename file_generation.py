import os

for i in range(1, 32):
    if str(i) not in os.listdir():
        os.mkdir(str(i))

    with open(f"{i}/input.txt", "w"):
        pass

    with open(f"{i}/main.py", "w") as file:
        template = f"with open('{i}/input.txt') as f:\n    lines = f.readlines()"
        file.write(template)
