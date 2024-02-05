import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter: row.code for (index, row) in data_frame.iterrows()}

def generate_phonetics():
    word = input("Enter a word : ").upper()
    try:
        my_list = [phonetic_dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetics()
    else:
        print(my_list)

generate_phonetics()
