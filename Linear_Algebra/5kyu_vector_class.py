"""Exercise: Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals method, to check that two vectors that have the same components are equal
Note: the test cases will utilize the user-provided equals method."""


#My Solution

class Vector:

    def __init__(self, coordinates):
        self.coordinates = coordinates

    def equals(self, vector_b):
        if self.coordinates == vector_b.coordinates:
            return True
        else:
            return False

    def add(self, vector_b):
        if len(self.coordinates) != len(vector_b.coordinates):
            raise ValueError("The vectors have different dimensions")

        new_coords = []
        for i in range(len(self.coordinates)):
            new_coord = self.coordinates[i] + vector_b.coordinates[i]
            new_coords.append(new_coord)

        return Vector(new_coords)

    def subtract(self, vector_b):
        if len(self.coordinates) != len(vector_b.coordinates):
            raise ValueError("The vectors have different dimensions")

        new_coords = []
        for i in range(len(self.coordinates)):
            new_coord = self.coordinates[i] - vector_b.coordinates[i]
            new_coords.append(new_coord)

        return Vector(new_coords)

    def dot(self, vector_b):
        if len(self.coordinates) != len(vector_b.coordinates):
            raise ValueError("The vectors have different dimensions")

        dot_sum = 0
        for i in range(len(self.coordinates)):
            dot_sum += self.coordinates[i] * vector_b.coordinates[i]

        return dot_sum

    def norm(self):
        squared_length = 0
        for i in range(len(self.coordinates)):
            squared_length += self.coordinates[i] ** 2

        length = squared_length ** (1 / 2)
        return length

    def __str__(self):
        string_coords = str(self.coordinates)
        new_string = string_coords.replace("[", "(").replace("]", ")").replace(" ", "")

        return f"{new_string}"
