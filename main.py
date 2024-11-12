import typing #GUI
shots = int(input("Shots 4 or 10:  "))
shots_in = int(input("Amount oif shots in: "))
a_price_no_margin = 13
b_price_no_margin = 14
c_price_no_margin = 6

a_price = 20
b_price = 20
c_price = 10

a_name = "Mini chupa chups"
b_name = "Mentos mini chupa chups mix"
c_name = "Sour straps"

def prize_pick(amount: int, cand: typing.List):
    if amount < min(a_price,b_price,c_price):
        return ["break"]
    print(f"{amount} left")
    def print_and_ask():
        if amount > a_price-1:
            print(f"{a_name} * {cand.count("a")}: {a_price}")
        if amount > b_price-1:
            print(f"{b_name} * {cand.count("b")}: {b_price}")
        if amount > c_price-1:
            print(f"{c_name} * {cand.count("c")}: {c_price}")
        x = str(input("enter option: "))
        return x
    x = print_and_ask()
    if x == "a":
        if amount > a_price-1:
            return ["a", a_price]
        else:
            print("not enough money!")
            return ["nanValue"]
    if x == "b":
        if amount > b_price-1:
            return ["b", b_price]
        else:
            print("not enough money!")
            return ["nanValue"]
    if x == "c":
        if amount > c_price-1:
            return ["c", c_price]
        else:
            print("not enough money!")
            return ["nanValue"]
    print("invalid value!")
    return ["nanValue"]
            
def prize_remove(cand: typing.List) -> str:
    def ask_and_recieve() -> str:
        if "a" in cand:
            print(f"a:{a_name} * {cand.count("a")}")
        if "b" in cand:
            print(f"b:{b_name} * {cand.count("b")}")
        if "c" in cand:
            print(f"c:{c_name} * {cand.count("c")}")
        x = str(input("what to remove? (z for cancel): "))
        return x
    x = ask_and_recieve()
    if x == "z":
        return ["nanValue"]
    if x == "a":
        if "a" in cand:
            return ["a"]
        else:
            print(f"no {a_name} in cart")
            return ["nanValue"]
    if x == "b":
        if "b" in cand:
            return ["b"]
        else:
            print(f"no {b_name} in cart")
            return ["nanValue"]
    if x == "c":
        if c in cand:
            return ["c"]
        else:
            print(f"no {c_name} in cart")
            return ["nanValue"]
    else:
        print("invalid value!")
        return ["nanValue"]



if shots == 4:
    max_amount = 100
    player_paid = 200
    money = (shots_in / shots)*max_amount
    og_money = money

            
if shots == 8:
    max_amount = 40
    player_paid = 400
    # max_amount = 11
    money = (shots_in / shots)*max_amount
    og_money = money





candy = []
while money > c_price-1:
    x = str(input("remove (r) or pick (p) or exit(x): "))
    if x != "r" and x != "p" and x != "x":
        continue
    if x == "p":
        ret = prize_pick(money, candy)
        if ret[0] == "break":
            break
        if ret[0] == "nanValue":
            continue
        money = money - ret[1]
        candy.append(ret[0])
    if x == "r":
        ret = prize_remove(candy)
        if ret[0] == ["nanValue"]:
            continue
        candy.remove(ret[0])
    if x == "x":
        break
a = 0
b = 0
c = 0
for lol in candy:
    if lol == "a":
        a += 1
    
    if lol == "b":
        b += 1
    
    if lol == "c":
        c += 1
        
print(f"{a} x {a_name}")
print(f"{b} x {b_name}")
print(f"{c} x {c_name}")

# with open("sales.txt", "a") as s:
#     if shots == 10:
#         paid = 2.5
#     else:
#         paid = 1
#     s.write(f"{(a*0.13) + (b * 0.14) + (c * 0.06)}|||{a} mini chupas, {b} mentos mini chupa chupas mix, {c} sour straps. Consumer paid ${paid}. Candy cost {(a*0.13) + (b * 0.14) + (c * 0.06)}. Total gain: {paid - ((a*0.13) + (b * 0.14) + (c * 0.06))}")
            
with open("sales.csv", "a") as f: #                                                                                                                                                                                                                      
    # f.write(f'"{a_name}",') # a name
    # f.write(f'"{b_name}",') # b name
    # f.write(f'"{c_name}",') # c name
    # f.write(f'"{a}",') # How much of a they recieved
    # f.write(f'"{b}",') # How much of b they recieved
    # f.write(f'"{c}",') # How much of c they recieved
    # f.write(f'"{a_price_no_margin / 100}",') # how much each of a cost us
    # f.write(f'"{b_price_no_margin / 100}",') # how much each of b cost us
    # f.write(f'"{c_price_no_margin / 100}",') # how much each of c cost us
    # f.write(f'"{a_price}",') # how much each of a "cost" to the consumers in credits
    # f.write(f'"{b_price}",') # how much each of b "cost" to the consumers in credits
    # f.write(f'"{c_price}",') # how much each of c "cost" to the consumers in credits
    # f.write(f'"{shots}",') # How many shots they bought
    # f.write(f'"{shots_in}",') # How many they actually got in
    # f.write(f'"{max_amount}",') # What was the max amount they could get in credits
    # f.write(f'"{og_money}",') # What did they get to "spend" in credits
    # f.write(f'"{((a * a_price_no_margin) + (b * b_price_no_margin) + (c * c_price_no_margin)) / 100}",') # how much the candy cost us total
    # f.write(f'"{(a * a_price) + (b * b_price) + (c * c_price)}",') # How much the consumers "spent"
    # f.write(f'"{player_paid - ((a * a_price_no_margin) + (b * b_price_no_margin) + (c * c_price_no_margin)) / 100}",') # how much we profited
    # f.write(f'"{money}",') # how much crdddits was left left over from the spree
    # f.write(f'"{player_paid/100}"') #how much the player paid to play
    # f.write(f'\n')

    # f.write(f'"{a_name}",')
    # f.write(f'"{b_name}",')
    # f.write(f'"{c_name}",')
    # f.write(f'"{a}",')
    # f.write(f'"{b}",')
    # f.write(f'"{c}",')
    # f.write(f'"{a_price_no_margin}",')
    # f.write(f'"{b_price_no_margin}",')
    # f.write(f'"{c_price_no_margin}",')
    # f.write(f'"{a_price}",')
    # f.write(f'"{b_price}",')
    # f.write(f'"{c_price}",')
    # f.write(f'"{shots}",')
    # f.write(f'"{shots_in}",')
    # f.write(f'"{max_amount}",')
    # f.write(f'"{og_money}",')
    # f.write(f'"{(a_price_no_margin*a)+(b_price_no_margin*b)+(c_price_no_margin*c)}",')
    # f.write(f'"{100-money}",')
    # f.write(f'"{player_paid/100}",')
    f.write(f'"{a_name}",')  # What is a called?
    f.write(f'"{b_name}",')  # What is b called?
    f.write(f'"{c_name}",')  # What is c called?
    f.write(f'"{a}",')  # How much of A did they want?
    f.write(f'"{b}",')  # How much of B did they want?
    f.write(f'"{c}",')  # How much of C did they want?
    f.write(f'"{a_price_no_margin / 100}",')  # How much did A cost us each?
    f.write(f'"{b_price_no_margin / 100}",')  # How much did B cost us each?
    f.write(f'"{c_price_no_margin / 100}",')  # How much did C cost us each?
    f.write(f'"{a_price}",')  # How much did A cost the consumer in credits?
    f.write(f'"{b_price}",')  # How much did B cost the consumer in credits?
    f.write(f'"{c_price}",')  # How much did C cost the consumer in credits?
    f.write(f'"{shots}",')  # How many shots did the consumer buy?
    f.write(f'"{shots_in}",')  # How many shots did the consumer get in?
    f.write(f'"{max_amount}",')  # What was the maximum amount of credits they could receive?
    f.write(f'"{og_money}",')  # What did they actually get to spend in credits?
    f.write(f'"{((a * a_price_no_margin) + (b * b_price_no_margin) + (c * c_price_no_margin)) / 100}",')  # How much did the candy cost us?
    f.write(f'"{(a * a_price) + (b * b_price) + (c * c_price)}",')  # How many credits did the consumer spend?
    f.write(f'"{money}",')  # How many credits did they not use?
    f.write(f'"{player_paid / 100}"')  # How much did they pay to play?
    f.write(f'\n')

