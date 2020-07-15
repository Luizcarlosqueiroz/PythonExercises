a = 1
b = 2

print(f"1, {a}, ",end="")
while b <= 500:
    print(b, end=", ")
    c = b
    b += a
    a = c