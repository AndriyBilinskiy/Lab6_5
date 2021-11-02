from typing import List
import random

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    grid = []
    for i in range(3):
        row = []
        for i in range(3):
            random_letter = chr(random.randint(ord('a'),ord('z')))
            row.append(random_letter)
        grid.append(row)
    return grid


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    str  = ''
    letters = str.join(letters)
    words_that_follow_rules = []
    central_letter = letters[4]
    data = ''
    with open("en.txt", 'r') as file:
        data = file.read()
    words = data.split('\n')
    for word in words:
        if not central_letter in word or len(word) < 4:
            continue
        word = word.lower()
        letters_copy = letters
        follows_rules = True
        for letter in word:
            if letter in letters_copy:
                letters_copy.replace(letter, '')
            else :
                follows_rules = False
                break
        if follows_rules:
            words_that_follow_rules.append(word)
    return words_that_follow_rules



def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    words = []
    print("Enter each word from the new line. Press ctrl+d to finish")
    while True:
        try:
            word = input('>>> ')
            words.append(word)
        except EOFError:
            break
    return set(words)


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    central_letter = letters[4]
    res = []
    for i in user_words:
        if not central_letter in i or len(i) < 4:
            continue
        word = i.lower()
        letters_copy = letters
        follows_rules = True
        for letter in word:
            if letter in letters_copy:
                letters_copy.replace(letter, '')
            else :
                follows_rules = False
                break
        if follows_rules and not word in words_from_dict:
            res.append(word) 
    return res


def results():
    grid = generate_grid()

    letters =''
    for i in grid:
        for j in i:
            letters += j
            print(j, end = ' ')
        print()
    user_words = list(get_user_words())
    dict_words = get_words('en.txt', letters)
    words_not_in_dict = get_pure_user_words(user_words, letters, dict_words)
    for i in words_not_in_dict:
        print(i,end=', ')
    if len(words_not_in_dict) > 0:
        print ("Hasn't been found in the dictionary")
    pass

