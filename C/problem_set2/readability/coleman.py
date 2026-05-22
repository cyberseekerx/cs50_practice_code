letter = int(input("letter: "))
words = int(input("words: "))
l = letter / words * 100
sen = int(input("sen: "))
s = sen / words * 100
index = 0.0588 * l - 0.296 * s - 15.8
print(index)
