grocery = {}
fruits = ["Avacado", "mango", "banana"]
dairy = ["milk", "cheese", "panner"]

converted_fruits = [item.upper() for item in fruits]
converted_dairy = [item.upper() for item in dairy]

##TODO do this and that

while True:
    try:
        item = input().upper()
    except EOFError:
        print()
        break
    count = grocery.setdefault(item, 0)
    grocery[item] = count + 1

for item, count in sorted(grocery.items()):
    if item in converted_fruits:
        category = "FRUITS"
    elif item in converted_dairy:
        category = "DAIRY"
    else:
        category = "OTHER"
    print(category, count, item)
