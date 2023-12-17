# Recursive function to find power of a number

print("1.Recursion function to find power of a number")
print("  --------------------------------------------")

def power(n,p):
    if p == 0:
        return 1
    return (n*power(n, p-1))
if __name__ == '__main__':
    n = 7
    p = 2

    print(power(n,p))

print()
print("*********************************************************************************")
print()

# 2.Using recursion function to get sum of digits

print("2.recursion on sum of digits")
print("   -------------------------")
def sum_of_digits(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        remaining_digits = n // 10
        return last_digit + sum_of_digits(remaining_digits)

result = sum_of_digits(12345)  # Calculates the sum of digits in 12345, which is 1+2+3+4+5 = 15
print(result)

print()
print("******************************************************************************************")
print()

# 3.write a python program to find sum of a nested list using recursion

print("3.Sum of nested list using recursion")
print("  ----------------------------------")

def nested_list(n):
    total = 0
    for j in range(len(n)):
        if type(n[j]) == list:
            total += nested_list(n[j])
        else:
            total += n[j]
    return total
print(nested_list([[1,2,3],[6,7],8]))