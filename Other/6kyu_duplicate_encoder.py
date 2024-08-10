# Challenge description
#
# The goal of this exercise is to convert a string to a new string
# where each character in the new string is "(" if that character appears only once in the original string,
# or ")" if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.
#
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("


# My solution:

def duplicate_encode(word):
    mult_letters = set()
    all_letters = list()
    for letter in word.lower():
        if letter in all_letters:
            mult_letters.add(letter)
        else:
            all_letters.append(letter)
    new_list = [")" if x in mult_letters else "(" for x in word.lower()]
    new_string = "".join(new_list)
    return new_string