# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
#main

with open("../../100_Days_Python/Mail Merger/Input/Names/invited_names.txt") as data:
    names = data.readlines()
    for name in names:
        i = names.index(name)
        names[i] = name.replace(name, name.strip())

with open("../../100_Days_Python/Mail Merger/Input/Letters/starting_letter.txt") as letter:
    txt = letter.read()

for name in names:
    f = open(f"../../100_Days_Python/Mail Merger/Output/ReadyToSend/{name}.txt", "w+")
    text = txt.replace('[name]', name)
    f.write(text)
    f.close()
