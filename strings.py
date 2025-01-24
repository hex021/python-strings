vowels = 'aeiouAEIOU'
input_str=input("Please enter your string:")
count_vowels=0
for char in input_str:
    if char in vowels:
        count_vowels+=1

print("Number of vowels:",count_vowels)
