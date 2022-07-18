class Vector3():
    """Implements a Vector3 class similar to that found in Unity."""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def __add__(self, other_vector) -> "Vector3":
        return Vector3(self.x + other_vector.x, self.y + other_vector.y, self.z + other_vector.z)

    def __sub__(self, other_vector) -> "Vector3":
        return Vector3(self.x - other_vector.x, self.y - other_vector.y, self.z - other_vector.z)

    def __mul__(self, partner) -> "Vector3":
        # Scales the vector.
        if isinstance(partner, int) or isinstance(partner, float):
            return Vector3(self.x * partner, self.y * partner, self.z * partner)
        # Returns the dot product.
        elif isinstance(partner, Vector3):
            return Vector3(self.x * partner.x, self.y * partner.y, self.z * partner.z)
        else:
            raise Exception(
                "A vector3 must be multiplied with a scalar or another Vector3.")

    def __eq__(self, partner) -> bool:
        return self.x == partner.x and self.y == partner.y and self.z == partner.z
