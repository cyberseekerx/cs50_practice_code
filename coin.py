import random

count = 0
head = 0
tails = 0
while True:
    coin = random.choice(["head", "tails"])
    if coin == "head":
        head += 1
    else:
        tails += 1

    count = count + 1
    if count >= 10000000:
        break

percentage_head = head / (head + tails) * 100
percentage_tails = tails / (head + tails) * 100
print()
print("count:", +count)
print()
print("Heads:", +head, f"({percentage_head:.2f}%)")
print("tails:", +tails, f"({percentage_tails:.2f}%)")
