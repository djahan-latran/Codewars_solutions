# Challenge description
#
# There exists a sequence of numbers that follows the pattern
#
#           1
#          11
#          21
#         1211
#        111221
#        312211
#       13112221
#      1113213211
#           .
#           .
#           .
# Starting with "1" the following lines are produced by "saying what you see",
# so that line two is "one one", line three is "two one(s)", line four is "one two one one".
#
# Write a function that given a starting value as a string,
# returns the appropriate sequence as a list.
# The starting value can have any number of digits.
# The termination condition is a defined by the maximum number of iterations, also supplied as an argument.


# My solution
def look_and_say(data='1', maxlen=5, result=None):
    if result is None:
        result = []

    # Base case
    if maxlen == 0:
        return result

    current_nums = ""
    current_consecutive = data[0]
    current_counter = 0

    for num in data:
        if num == current_consecutive:
            current_counter += 1
        else:
            current_nums += str(current_counter)
            current_nums += current_consecutive
            current_consecutive = num
            current_counter = 1
    current_nums += str(current_counter)
    current_nums += current_consecutive

    print(f"These are the current nums: {current_nums}")

    result.append(current_nums)

    return look_and_say(current_nums, maxlen - 1, result)