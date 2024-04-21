def add_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"


result1 = add_tags('i', 'Python')
result2 = add_tags('b', 'Python Tutorial')

print("Result 1:", result1)
print("Result 2:", result2)
