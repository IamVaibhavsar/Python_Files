# Convert all vowels in the string to v OR V

def translate(string):
    translation=""
    for letter in string:
        if letter in "aeiouAEIOU":
            translation=translation+"v"
        else:
                translation=translation+letter
    return translation

str=input("Enter the string that you want to translate:")
print(translate(str))


