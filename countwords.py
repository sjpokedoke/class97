introduction = input("Write an introduction about yourself!")
characters = 0
words = 1
for i in introduction:
    characters = characters+1
    if (i==" "):
        words = words+1
print("Number of words in the text: ")
print(words)
print("Number of characters in the text: ")
print(characters)