#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# with open(r"F:\code\udemy\day24\mail_merge\Input\Letters\starting_letter.txt", mode="r") as letter_file:
#     content = letter_file.read()
#     print(content)

from os import system

def clear():
    system("cls")

clear()

# obtains each name from text file, separated
with open(r"F:\code\udemy\day24\mail_merge\Input\Names\invited_names.txt", mode="r") as name_file:
    name_content = name_file.readlines()

# obtains contents of the letter template
with open(r"F:\code\udemy\day24\mail_merge\Input\Letters\starting_letter.txt", mode="r") as letter_file:
    letter_content = letter_file.read()
    
# # personalized letters to each individual
for name in name_content:
    name = name.strip()
    with open(f"F:\\code\\udemy\\day24\\mail_merge\\ReadyToSend\\{name}_letter", mode="w") as new_letter:
        new_letter.write(letter_content.replace("[name]", f"{name}"))