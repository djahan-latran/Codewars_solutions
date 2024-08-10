# Build Tower
# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors.
# A tower block is represented with "*" character.
#
# For example, a tower with 3 floors looks like this:
#
# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]
# And a tower with 6 floors looks like this:
#
# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]


"""My solution"""

def tower_builder(n_floors, star_counter=None, tower=None):
    # for each additional floor there are n-1 spaces on each side of the stars on the first floor
    # for each additional floor there are +2 additional stars and -2 spaces (+1 star,-1 space on each side)
    if tower is None:
        tower = []

    if star_counter is None:
        star_counter = 1

    # Base case
    if n_floors <= 0:
        return tower

    floor = ""

    for i in range(n_floors - 1):
        floor += " "
    floor += "*" * star_counter
    for i in range(n_floors - 1):
        floor += " "

    tower.append(floor)
    star_counter += 2

    return tower_builder(n_floors - 1, star_counter, tower)