# 7. Write a python function to remove a given word from a list and strip it at the same time.
list = ["apple", "mango", "Banana", "guava", "grapes"]
def strip_word(lst, word):
    word = word.strip()  # Ensure the input word is stripped
    return [item for item in lst if item.strip() != word]  # Filter out the word

word = input("Enter a word you want to remove: ")
a = strip_word(list, word)
print(a)

# b = "neha"
# print(b.strip("a"))