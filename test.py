""" MiasDealerShop = [
    {"Item": "1. ella's poopy shoes", "price": 0.56, "description": "During a fire drill, third period, Ella step into some not so good, solid brown substance. It was unfortunate But thankfully she was able to wash it off! However, there may be some residue in the creases of her shoes."},                                                           
    {"Item": "2. olivia's cat's hairballs", "price": 4.99, "description": "Olivia is allergic to cats, however, she still has two very adorable cats, Ollie and Ellie! Her cats are kinda hairy and she just has a bunch of hair stuck around her home."},
    {"Item": "3. BigBackLiver's Gooner Fanfic(resale)", "price": 350.00, "description": "Collaboration with BigBack Liver's Library!! Buy now before it's too late..."},
    {"Item": "4. Tina's BrainRot Guide", "price": 6.99, "description": "Tina has so much brainrot saved in her brain that it makes me feel way old even though im literally the same age as her."},
    {"Item": "5. Xingwing's 12 pc Soggy Chicken Wing", "price": 12.99, "description": "Xingwing is a nickname. She also sells wings but they're old and molding and smelly..."}, 
    {"Item": "6. Maggie's fat jokes about her ex", "price": 0, "description": "Uhm so they ever existsed!"},
    {"Item": "7. Mia's Fresh Cut Grass", "price": 68.99, "description": "Fresh Cut Grass from my backyard!!"}
]

for i in range(0, len(MiasDealerShop)):
    print(MiasDealerShop[i]["Item"])
Cart = input("What would you like to buy?") """

def language(x): 
    x = x.lower()
    scount = x.count("s")
    tcount = x.count("t")
    if scount > tcount:
        print("English")
    elif tcount >= scount:
        print("French")
    else:
        print("huh")
language("ella")