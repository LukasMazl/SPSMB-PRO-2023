MONEY = (5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1)

user_account = int(input("Write an amount: "))

for item in MONEY:
    count = user_account // item
    user_account = user_account % item
    if count != 0:
        print(f"{item}kc x {count}")