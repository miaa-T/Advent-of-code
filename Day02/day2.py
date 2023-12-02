import re

file_path = 'Games.txt'
max_numbers = {'green': 0, 'red': 0, 'blue': 0}  # Initialize with default values
i = 0
line_count = 0

try:
    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
            pattern = re.compile(r'^Game \d+: ')
            result = re.sub(pattern, '', line)

            occurrences_green = re.findall(r'(\d+)\s+green\b', line)
            numbers_green = [int(num) for num in occurrences_green]
            max_numbers['green'] = max(numbers_green)

            occurrences_red = re.findall(r'(\d+)\s+red\b', line)
            numbers_red = [int(num) for num in occurrences_red]
            max_numbers['red'] = max(numbers_red)

            occurrences_blue = re.findall(r'(\d+)\s+blue\b', line)
            numbers_blue = [int(num) for num in occurrences_blue]
            max_numbers['blue'] = max(numbers_blue)
            #print( max_numbers['green'] ,  max_numbers['red'],  max_numbers['blue'])
            if max_numbers['green'] <= 13 and max_numbers['red'] <= 12 and max_numbers['blue'] <= 14:
              i = i + line_count
              print(i)
    print(f"The sum of the IDs of those games is : {i}")
except FileNotFoundError:
    print(f"The file at path '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")



