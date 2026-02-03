import random
from os.path import exists
def createFile():
    words={"python","patata","manzana","pimiento"}
    archivo = open('words.txt', 'w')
    if exists('words.txt'):
        for word in words:
            archivo.write(word+"\n")
    archivo.close()
    archivo = open('prueba.txt', 'a')
    archivo.write('cebolla')
    archivo.close()
def game():
    print("WELCOME TO WORD GUESSER")
    archivo = open('words.txt', 'r')
    palabras=archivo.readlines()
    word=random.choice(palabras)
    guesses=0
    hasWon=0
    guessed_letters = set()
    print("_ " * (len(word)-1))
    while guesses!=0 or hasWon!=1:
        guess = input("\nEnter a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.add(guess)
        if guess in word:
            print("Good guess!")
        else:
            guesses += 1
            print(f"Wrong! You have {len(word)-guesses} attempts left.")

        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        word_display.remove(word_display[len(word)-1])
        print(" ".join(word_display))
        if "_" not in word_display:
            print("\nYou guessed the word: ", word)
            break
#main
createFile()
game()

