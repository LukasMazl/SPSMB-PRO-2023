a = int(input("Write A index: "))
b = int(input("Write B index: "))
c = int(input("Write C index: "))

D = b**2 - 4 * a * c

if D > 0:
    x1 = (-b - D**(1/2)) / (2 * a)
    x2 = (-b + D**(1/2)) / (2 * a)
    print(f"The solution for x1 = {x1}")
    print(f"The solution for x2 = {x2}")
elif D == 0:
    x1 = (-b) / (2 * a)
    print(f"The solution for x1 = {x1}")
else:
    print(f"({-b} - {-D}^(1/2)) * i / ({2 * a})")
    print(f"({-b} + {-D}^(1/2)) * I / ({2 * a})")