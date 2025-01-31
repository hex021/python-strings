number = int(input("Enter a number: "))

is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

is_perfect = sum(i for i in range(1, number) if number % i == 0) == number
is_armstrong = sum(int(digit) ** len(str(number)) for digit in str(number)) == number
is_palindrome = str(number) == str(number)[::-1]
is_automorphic = str(number * number).endswith(str(number))

print("Is Prime:", is_prime)
print("Is Perfect:", is_perfect)
print("Is Armstrong:", is_armstrong)
print("Is Palindrome:", is_palindrome)
print("Is Automorphic:", is_automorphic)