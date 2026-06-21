# Problem 4

char = input("Enter a character: ")
lower_char = char.lower()

if lower_char in ['a', 'e', 'i', 'o', 'u']:
    print(f"'{char}' is a Vowel.")
else:
    print(f"'{char}' is Not a Vowel.")
