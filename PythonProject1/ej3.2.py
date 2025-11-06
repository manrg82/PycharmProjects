import random

def hangman():
    words = ["python", "programming", "developer", "hangman", "challenge", "computer"]
    secret_word = random.choice(words)
    guessed_letters = set()
    lives = 6

    print("Welcome to Hanged!")
    print("_ " * len(secret_word))

    while lives > 0:
        guess = input("\nEnter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            lives -= 1
            print(f"Wrong! You lose a life. Lives left: {lives}")

        word_display = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print(" ".join(word_display))

        if "_" not in word_display:
            print("\nYou guessed the word:", secret_word)
            break
    else:
        print("\n💀 You lost! The word was:", secret_word)


hangman()
