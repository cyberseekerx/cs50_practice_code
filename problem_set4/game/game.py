import random, sys
while True:
    try:
        level = int(input("Level: "))
        if level < 0:
            continue
        break
    except EOFError:
        sys.exit()
    except:
        continue

num = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
    except EOFError:
        sys.exit()
    except:
        continue
    if num > guess:
        print("Too small!")
    elif num < guess:
        print("Too large!")
    else:
        print("Just right!")
        sys.exit()

