"""
SWYPE KEYBOARD

    QWERTY keyboard

    Lowercase a-z only, no whitespace or punctuation

    The first and last characters of the input string will always match the first and last characters of the desired output word

    Don't assume users take the most efficient path between letters

    Every letter of the output word will appear in the input string
    
    ============================

    Double letters in the output word might appear only once in the input string, e.g. "polkjuy" could yield "polly".
    Make your program handle this possibility.
"""
import timeit

MIN_LENGTH = 5
WORD_POOL = []

with open("./files/284.words.txt", "r") as f:
    # reading file is an heavy IO operation
    # create the word pool in the memory
    lines = f.readlines()
    WORD_POOL = [line[:-1] for line in lines if len(line) > 5]


def get_start_end_matching_words(input, word_list=WORD_POOL):
    # give input q ... n, we return all matching words with those start/end flags
    return filter(lambda x: x[0] == input[0] and x[-1] == input[-1], WORD_POOL)


def get_proper_sequence(word, input):
    # returns true if the sequence of letters in the word matches their position in the input.
    last_id = 0
    for letter in word:
        if letter not in input[last_id:]:
            return False
        last_id += input[last_id:].index(letter)
    return True


def possible_words(input):
    selected_pool = get_start_end_matching_words(input)
    return filter(lambda x: get_proper_sequence(x, input), selected_pool)


def derived_words(input):
    return list(possible_words(input))


def check():
    one = derived_words("qwertyuytresdftyuioknn")
    for each in "queen question".split(" "):
        assert each in one
    two = derived_words("gijakjthoijerjidsdfnokg")
    for each in "gaeing garring gathering gating geeing gieing going goring".split(" "):
        assert each in two


if __name__ == "__main__":
    check()
    # print(timeit.timeit("check()", setup="from __main__ import check", number=10)/10)
