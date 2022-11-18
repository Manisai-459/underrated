def add_karo(a, b):
    if b == 0:
        return a
    return add_karo(a ^ b, (a & b) << 1)


a = list(map(int, input("Enter two numbers : ").split()))
print(add_karo(a[0], a[1]))
