greating = str(input("greating: "))
lowered_greating = greating.lower()
if lowered_greating.startswith ("") :
    print("$0")
elif  lowered_greating.startswith("h"):
    print("$20")
else :
    print("$100")
