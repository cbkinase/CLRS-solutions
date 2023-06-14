# Given: a set of functions F and a number T.
# Problem: find the largest input size N for F such that F(N) < T

import math

def binary_search_largest(F, T, low, high):
    largest_input = None

    while low <= high:
        mid = (low + high) // 2
        result = F(mid)

        if result < T:
            largest_input = mid
            low = mid + 1
        else:
            high = mid - 1

    return largest_input

def x_squared(x):
    return x**2

def x_cubed(x):
    return x**3

def two_to_the_n(x):
    return 2**x

def log_base_2_n(x):
    return math.log(x, 2)

def square_root(x):
    return math.sqrt(x)

def identity(x):
    return x

def log_linear(x):
    return x * log_base_2_n(x)

func_struct = [
    {"fn": identity, "guess": 2**63-1},
    {"fn": log_linear, "guess": 2**63-1},
    {"fn": x_squared, "guess": 2**63-1},
    {"fn": x_cubed, "guess": 2**63-1},
    {"fn": two_to_the_n, "guess": 100000},
    {"fn": math.factorial, "guess": 100000},
] # sqrt n and lg n overflow :( - may fix later

base_num = 1_000_000
target_vals = [base_num, base_num*60, base_num*60*60, base_num*60*60*24, base_num*60*60*24*30, base_num*60*60*24*30*12, base_num*60*60*24*30*12*100]

for val in target_vals:
    print("")
    print(val)
    print("")
    for f in func_struct:
        N = binary_search_largest(f.get('fn'), val+1, 0, f.get('guess'))
        print(f"Largest input size N: {N} for function {f.get('fn').__name__}")
