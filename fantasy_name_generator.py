import random

MAX_WORD_LENGTH = 15
NUMBER_OF_NAMES = 50

with open('DATA/words.txt') as words_in:
    all_words = [word.rstrip() for word in words_in if len(word) <= MAX_WORD_LENGTH]

raw_words = random.sample(all_words, NUMBER_OF_NAMES)

fantasy_names = ["".join(reversed(word)) for word in raw_words]

for fantasy_name in fantasy_names:
    print(fantasy_name)

