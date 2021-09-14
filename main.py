import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
panda = pandas.read_csv('./nato_phonetic_alphabet.csv')

phonetic_alphabet = {row.letter:row.code for (index, row) in panda.iterrows()}


def generate_phonetic():
    user_input_name = input("Please enter your name: ").upper()
    try:
        phonetic_alphabet_list = [phonetic_alphabet[letter] for letter in list(user_input_name)]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_alphabet_list)


generate_phonetic()
