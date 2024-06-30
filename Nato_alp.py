import pandas 

# Read the CSV file into a DataFrame
df = pandas.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary from the DataFrame
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# Get a word from the user
user_input = input("Enter a word: ").upper()

# Create a list of phonetic code words
phonetic_code_words = [nato_dict[letter] for letter in user_input if letter in nato_dict]

print(phonetic_code_words)
