import timeit
import random


def OTHER_BIN_INT_ADD(A, B, n):
    C = [0] * (n + 1)
    carry = 0

    for i in range(n-1, -1, -1):
        digit_sum = A[i] + B[i] + carry
        C[i + 1] = digit_sum % 2
        if digit_sum > 1:
            carry = 1
        else:
            carry = 0

    C[0] = carry
    return C


def ADD_BINARY_INTEGERS_BITWISE(A, B, n):
    C = [0] * (n + 1)  # Initialize the result array C with n+1 elements
    carry = 0  # Initialize the carry variable to 0

    for i in range(n-1, -1, -1):
        # Compute the sum of A[i], B[i], and the carry
        digit_sum = A[i] ^ B[i] ^ carry
        # Determine the current digit of the sum
        C[i+1] = digit_sum
        # Update the carry for the next iteration
        carry = (A[i] & B[i]) | (B[i] & carry) | (A[i] & carry)
    # If there is a remaining carry, store it in the most significant digit of the result
    if carry != 0:
        C[0] = carry
    else:
        # Remove the extra leading zero in the result
        C = C[1:]

    return C


def ADD_BINARY_INTEGERS(A, B, n):
    C = [0] * (n + 1)  # Initialize the result array C with n+1 elements
    carry = 0  # Initialize the carry variable to 0

    for i in range(n-1, -1, -1):
        # Compute the sum of A[i], B[i], and the carry
        digit_sum = A[i] + B[i] + carry
        # Determine the current digit of the sum
        C[i+1] = digit_sum % 2
        # Update the carry for the next iteration
        carry = digit_sum // 2
    # If there is a remaining carry, store it in the most significant digit of the result
    if carry != 0:
        C[0] = carry
    else:
        # Remove the extra leading zero in the result
        C = C[1:]

    return C


n = 100
a = [random.randint(0, 1) for _ in range(n)]
b = a[:]

execution_time_bitwise = timeit.timeit(lambda: ADD_BINARY_INTEGERS_BITWISE(a, b, n), number=100_000)
execution_time = timeit.timeit(lambda: ADD_BINARY_INTEGERS(a, b, n), number=100_000)
execution_time_new = timeit.timeit(lambda: OTHER_BIN_INT_ADD(a, b, n), number=100_000)

print(execution_time_bitwise)
print(execution_time)
print(execution_time_new)

print(ADD_BINARY_INTEGERS_BITWISE(a, b, n))
print(ADD_BINARY_INTEGERS(a, b, n))
print(OTHER_BIN_INT_ADD(a, b, n))
