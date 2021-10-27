class Vector:
    """Represent a vector in multidimensional space."""

    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, key, value):
        self._coords[key] = value

    def __add__(self, other):
        if (len(self)) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for i in range(len(result)):
            result[i] = self._coords[i] + other[i]
        return result

    def __eq__(self, other):
        return self._coords == other.getCoords()

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


v1 = Vector(2)
print(v1)
v1[0] = 1
v1[1] = 2
print(v1)

v2 = Vector(2)
v2[0] = 3
v2[1] = 4

print(v2)

print(v1 + v2)