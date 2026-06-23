import random

#constants
player_life_initial = 6

#words list

words = [
    "apple", "jungle", "cactus", "blizzard", "trophy",
    "eclipse", "walrus", "chimney", "frenzy", "goblin",
    "sphinx", "quarry", "vortex", "plumber", "jigsaw",
    "oyster", "dwarf", "kazoo", "cryptic", "muffin"
]



#opening prompt
print("Welcome to Hangman! Here You have 6 lives to guess the word correctly")

def choose_word():
    selected_word = random.choice(words)
    return selected_word

def display_word(word, guessed):
    return " ".join(letter if letter in guessed else "_" for letter in word) 

def hangman():
    word = choose_word()
    guessed = set()
    lives = player_life_initial
    
    while lives > 0:
        print(f"\n{display_word(word, guessed)}  | Lives: {lives}")
        guess = input("Guess a letter:").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Single letter only.")
        elif guess in guessed:
            print("Already gussed")
        elif guess in word:
            guessed.add(guess)
            if all(l in guessed for l in word):
                print("You won! Word: {word}")
                return
        else:
            guessed.add(guess)
            lives -= 1
            print(f"Wrong! Lives left: {lives}")
    print(f"You lost! Word: {word}")

hangman()