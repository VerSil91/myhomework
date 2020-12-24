def int_func(word):
    latin_characters = "abcdefghijklmnopqrstuvwxyz"
    return word.title() if not set(word).difference(latin_characters) else False


words = input("Input words with 'space': ").split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), " ")
