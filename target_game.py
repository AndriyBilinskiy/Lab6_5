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
    words_that_follow_rules = []
    central_letter = letters[4]
    
    letters_counted = [0 for i in range(30)]
    for i in letters:
        letters_counted[ord(i) - 97] += 1
    with open('en.txt') as f:
        for word in f:
            word = word.lower()
            if word.find(central_letter) == -1:
                continue
            letters_counted_copy = letters_counted
            need_to_continue = False
            for letter in word:
                print (ord(letter))
                cur_leetter_position = ord(letter) - 97
                print(letters_counted_copy)
                print(cur_leetter_position)
                letters_counted_copy[cur_leetter_position] -= 1
                if letters_counted_copy[cur_leetter_position] < 0:
                    need_to_continue = True
                    break
            if need_to_continue:
                continue
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
    words_to_check = []
    central_letter = letters[4]
    res = []
    return res


def results():
    grid = generate_grid()

    letters =''
    for i in grid:
        for j in i:
            letters += j
            print(j, end = ' ')
        print()
    user_words = get_user_words()
    dict_words = get_words('en', letters,)
    words_not_in_dict = get_pure_user_words(user_words, letters, dict_words)
    for i in words_not_in_dict:
        print(i,end=', ')
    print ("Hasn't been found in the dictionary")
    pass
results()