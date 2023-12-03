with open('1/input.txt') as f:
  lines = f.readlines()

cardinal_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
reversed_numbers = [numstring[::-1] for numstring in cardinal_numbers]

def extract_first_number(line, numstrings):
  current_sequence = ""

  for ch in line:
    if ch.isnumeric():
      return int(ch)
      
    current_sequence += ch

    if current_sequence in numstrings:
      return numstrings.index(current_sequence)

    if any([numstr.startswith(current_sequence) for numstr in numstrings]):
      continue
    else:
      current_sequence = current_sequence[1:]

def number_from_line(line):
  reversed_line = line[::-1]
  first = extract_first_number(line, cardinal_numbers)
  second = extract_first_number(reversed_line, reversed_numbers)
  return first*10 + second

print(sum([number_from_line(line) for line in lines]))