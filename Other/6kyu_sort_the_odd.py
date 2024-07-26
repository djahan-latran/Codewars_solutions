# Challenge description
#
# You will be given an array of numbers.
# You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
#
# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


# My solution
def sort_array(source_array):
    s = source_array

    for i in range(len(s)):
        if s[i] % 2 != 0:
            min_index = i
            for j in range(i + 1, len(s)):
                if s[j] < s[min_index] and s[j] % 2 != 0:
                    min_index = j
            s[i], s[min_index] = s[min_index], s[i]

    return s