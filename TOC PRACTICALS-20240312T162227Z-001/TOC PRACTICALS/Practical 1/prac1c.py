import re 
my_text = input("Enter a string for tokenization: ")
print("Tokenization of a given input: ")
pattern = re.compile('\w+')

matches = pattern.finditer(my_text)

for token in matches:
    print(token)