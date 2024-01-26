import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter: row.code for (index, row) in data_frame.iterrows()}

word = input("Enter a word : ").upper()

my_list = [phonetic_dictionary[letter] for letter in word]

print(my_list)
