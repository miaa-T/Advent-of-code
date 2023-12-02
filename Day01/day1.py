file_path = 'calibrationDocument.txt'
result= 0
try:
    with open(file_path, 'r') as file:
        # Read the file line by line
        for line in file:
            for char in line:
             if char.isdigit():
              first_integer = char
            for char in reversed(line):
             if char.isdigit():
              last_integer = char
            value=int(last_integer+first_integer)
            result=result+value
            
    print(result)  # strip() removes newline characters at the end of each line  
except FileNotFoundError:
    print(f"The file at path '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

    
