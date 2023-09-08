value = int(input("Write a number: "))

x_prev = value / 2
for i in range(10):
    xn = (x_prev + value/x_prev)/2
    print(xn)
    x_prev = xn