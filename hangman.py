import random

word_list = ["tiger", "horse", "lion"]
chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)


display = []
for _ in range(word_length):
    display += "_"


end_of_game = False

while not end_of_game:
    guess = input("guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print("you win")