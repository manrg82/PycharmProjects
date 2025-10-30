#ej1
name = input("Please enter your name: ")
sales_input = input("Please enter your total sales for the month: ")

sales = float(sales_input)
commission_rate = 0.13
commission_amount = sales * commission_rate

commission_rounded = round(commission_amount, 2)

print(f"Hello {name}, your commission for this month is ${commission_rounded}.")
#ej2
text = input("Please enter a text: ")
letter1 = input("Enter the first letter: ")
letter2 = input("Enter the second letter: ")
letter3 = input("Enter the third letter: ")
text_lower = text.lower()
count1 = text_lower.count(letter1.lower())
count2 = text_lower.count(letter2.lower())
count3 = text_lower.count(letter3.lower())

print("\n--- Letter Count ---")
print(f"The letter '{letter1}' appears {count1} times.")
print(f"The letter '{letter2}' appears {count2} times.")
print(f"The letter '{letter3}' appears {count3} times.")
words = text.split()
word_count = len(words)

print("\n--- Word Count ---")
print(f"The total number of words in the text is: {word_count}")
first_letter = text[0]
last_letter = text[-1]

print("\n--- First & Last Letter ---")
print(f"The first letter of the text is '{first_letter}'.")
print(f"The last letter of the text is '{last_letter}'.")
reversed_text = text[::-1]

print("\n--- Reversed Text ---")
print(f"The text in reverse order is: {reversed_text}")
contains_python = 'python' in text_lower
python_answer = {
    True: "Yes, the word 'Python' appears in the text.",
    False: "No, the word 'Python' does not appear in the text."
}

print("\n--- Python Check ---")
print(python_answer[contains_python])
