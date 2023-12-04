import os

for i in range(3, 32):
    if str(i) not in os.listdir():
        os.mkdir(str(i))

    with open(f"{i}/input.txt", "w"):
        pass

    with open(f"{i}/main.py", "w") as file:
        template = f"with open('{i}/input.txt') as f:\n    lines = [line.rstrip() for line in f]"
        file.write(template)
