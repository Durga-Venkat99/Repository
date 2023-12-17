def myfun(x):
    return x[::-1]

text = myfun("hello this is venkat")
print(text)

text = ("who","are","you")[::-1]
print(text)

text = ("who", "are", "you")
reversed_words = [word[::-1] for word in text]
reversed_text = ' '.join(reversed_words)
print(reversed_text)