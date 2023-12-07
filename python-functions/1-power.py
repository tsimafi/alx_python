#!/usr/bin/env python3
def pow(a, b):
    # Base case: any number to the power of 0 is 1
    if b == 0:
        return 1
    # If the exponent is negative, calculate the reciprocal
    elif b < 0:
        return 1 / pow(a, -b)
    else:
        result = 1
        # Multiply 'a' by itself 'b' times
        for _ in range(b):
            result *= a
        return result

y = pow(2, -3)
print(y)