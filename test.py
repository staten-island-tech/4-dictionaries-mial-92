MiasDealerShop = [
    {"Item": "1. ella's poopy shoes", "price": 0.56, "description": "During a fire drill, third period, Ella step into some not so good, solid brown substance. It was unfortunate But thankfully she was able to wash it off! However, there may be some residue in the creases of her shoes."},                                                           
    {"Item": "2. olivia's cat's hairballs", "price": 4.99, "description": "Olivia is allergic to cats, however, she still has two very adorable cats, Ollie and Ellie! Her cats are kinda hairy and she just has a bunch of hair stuck around her home."},
    {"Item": "3. BigBackLiver's Gooner Fanfic(resale)", "price": 350.00, "description": "Collaboration with BigBack Liver's Library!! Buy now before it's too late..."},
    {"Item": "4. Tina's BrainRot Guide", "price": 6.99, "description": "Tina has so much brainrot saved in her brain that it makes me feel way old even though im literally the same age as her."},
    {"Item": "5. Xingwing's Twelve pc Soggy Chicken Wing", "price": 12.99, "description": "Xingwing is a nickname. She also sells wings but they're old and molding and smelly..."}, 
    {"Item": "6. Maggie's fat jokes about her ex", "price": 0, "description": "Uhm so they ever existsed!"},
    {"Item": "7. Mia's Fresh Cut Grass", "price": 68.99, "description": "Fresh Cut Grass from my backyard!!"}
]

for i in range(0, len(MiasDealerShop)):
    print(MiasDealerShop[i]["Item"])
Cart = input("What would you like to buy?")

consent = True

while consent == True:
    for item in MiasDealerShop:
        if Cart in item["Item"]:
            print(f"{item["Item"]} has been added to your cart")
            consent = input("Would you like to add more into your cart? ")
            if consent == "yes":
                Cart = input("What else would you like to buy?")
                Cart = Cart + 1
                consent = True
            if consent == "no":
                print("Ok! Time to check out.") 
    print(f"You are purchasing these items: ")
