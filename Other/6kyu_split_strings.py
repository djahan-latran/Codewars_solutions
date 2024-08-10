# Challenge Description
# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters
# then it should replace the missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']


# My solution
def solution(s):
    n = 2
    pairs = []

    for i in range(0, len(s) - 1, n):
        pairs.append(s[i:i + 2])
    if len(s) % 2 != 0:
        pairs.append(s[-1] + "_")
    return pairs