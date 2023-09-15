import random

COUNT_OF_ITERATION = 10_000
COUNT_OF_IN_CIRCLE = 0

def generate_position():
    return (random.random() - 0.5, random.random() - 0.5)

for _ in range(COUNT_OF_ITERATION):
    x, y = generate_position()
    if x ** 2 + y ** 2 <= 0.25:
        COUNT_OF_IN_CIRCLE += 1
    
P = COUNT_OF_IN_CIRCLE / COUNT_OF_ITERATION

print(f"Pi = {P * 4}")