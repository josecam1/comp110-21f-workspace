"""An example function definition."""


def my_max(a: int, b: int) -> int:
    """Returns the largest argument."""
    if a >= b:
        return a
    else:
        return b


x: int = 6
y: int = 5 + 2
z: int = my_max(x, y)
print(z)

# line 4: function signature
# line 14 function call