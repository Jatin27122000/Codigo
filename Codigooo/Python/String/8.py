l = ['Python', 'programming', 'Exercises', 'solution']
longest_word = ""
longest_length = 0

for word in l:
    # Check if the current word is longer than the previously found longest word
    if len(word) > longest_length:
        # Update the longest word and its length
        longest_word = word
        longest_length = len(word)

print("Longest word:", longest_word)
print("Length of the longest word:", longest_length)