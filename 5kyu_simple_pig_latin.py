"""
Move the first letter of each word to the end of it,
then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !"""


# My solution

def pig_it(text):
    splitted = text.split(" ")

    piglatin_str = ""
    counter = len(splitted) - 1

    for word in splitted:
        if "!" in word:
            new_word = "!"
        elif "?" in word:
            new_word = "?"
        elif "." in word:
            new_word = "."
        else:
            new_end = word[0] + "ay"
            new_word = word[1:] + new_end

        if counter > 0:
            piglatin_str += new_word + " "
        else:
            piglatin_str += new_word
        counter -= 1

    return piglatin_str
