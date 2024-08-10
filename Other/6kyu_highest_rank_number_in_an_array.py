# Challenge description
#
# Complete the method which returns the number which is most frequent in the given input array.
# If there is a tie for most frequent number, return the largest number among them.
#
# Note: no empty arrays will be given.
#
# Examples
# [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
# [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3


# My solution
def highest_rank(arr):
    dict = {}

    for number in arr:
        if number in dict:
            dict[number] += 1
        else:
            dict[number] = 1

    max_value = max(dict.values())

    max_numbers = [key for key, value in dict.items() if value == max_value]

    return max(max_numbers)