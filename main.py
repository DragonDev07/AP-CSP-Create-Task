import json

dictionary = []
matching_words = []

# Get Dictionary from Json file and make it a list (dictionary)
with open('dict.json', 'r') as f:
    dictionary = json.loads(f.read())

# Function that searches for word using parameters which are the user's input
def search_word(length, chars, length_letters):
    for word in dictionary:
        if len(word) == length:
            if word[-length_letters::] == chars:
                matching_words.append(word)

# Welcome the user!
print("Hello, and Welcome to the thing that gives you words ending in a letter of a given length")
print("You will get two prompts, one after the other.")
print("The first one will ask the length of the word")
print("The second will ask you the ending letter")
print("Enjoy!")
print("--------------------------------------------------------------------------------------------------")

# Get the users input for length and ending letter
user_length = int(input("Enter Length of words to search for: "))
ending_with = input("Enter a (or multiple) latter(s) that the words will end with (ex. 'a' or 'abc'): ")
ending_with = ending_with.lower() # Make sure the ending letter value is lowercase so that the dict doesnt mess up, even if the user enters caps.
print("--------------------------------------------------------------------------------------------------")
print("Words: ")

# Call search_word function to search for matching words
search_word(user_length, ending_with, len(ending_with))

# Check if the length of the matching words list is 0, if it is, print no matching words.
if len(matching_words) == 0:
    print("There are no matching words!")
else: # If the length is not 0, print out each matching word on a seperate line
    for word in matching_words:
        print(word)
