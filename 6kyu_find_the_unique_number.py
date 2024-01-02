# Challenge description
#
# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.


# My solution
def find_uniq(arr):
    if arr[0] != arr[1] and arr[0] != arr[2]:
        return arr[0]
    elif arr[-1] != arr[-2] and arr[-1] != arr[-3]:
        return arr[-1]
    else:
        for i in range(len(arr)):
            if arr[i] != arr[i + 1] and arr[i] != arr[i - 1]:
                return arr[i]
