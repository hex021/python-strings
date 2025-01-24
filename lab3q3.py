string_1 = input("Enter the string 1: ")
string_2= input("Enter the string 2: ")

if string_2 in string_1:
    print(f'"{string_2}" is found in "{string_1}".')
else:
    print(f'"{string_2}" is not found in "{string_1}".')