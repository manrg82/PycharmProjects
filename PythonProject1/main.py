
sentence = input("Enter a sentence: ").lower()

letters = []
for i in range(3):
    letter = input(f"Enter letter {i+1}: ").lower()
    while len(letter) != 1 :
        letter = input("Please enter a single letter: ").lower()
    letters.append(letter)

print("\nLetter counts:")
for letter in letters:
    count = sentence.count(letter)
    print(f"'{letter}' appears {count} time(s) in the sentence.")

word_count = len(sentence.split())
print(f"\nTotal word count: {word_count}")

first_letter = sentence[0]
print(f"The first letter of your sentence is: '{first_letter}'")