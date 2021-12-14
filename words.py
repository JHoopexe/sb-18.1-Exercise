
def print_upper_words(words,char1,char2):
    """Enter array of words & letters and returns words that start with those letters"""
    for x in words:
        if x[0].lower() == char1.lower() or x[0].lower() == char2.lower():
            print(x.upper())

print_upper_words(["hello","hey","goodbye","yo","yes", "buenas dias"], "g", "b")
