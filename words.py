def print_upper_words(words, must_start_with={"e"}):
    newWords = []
    for word in words:
        if word[0] in must_start_with:
            caps = word.upper()
            newWords.append(caps)
    print(newWords)

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})