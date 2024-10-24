shots = int(input("Shots 4 or 10:  "))
shots_in = int(input("Amount oif shots in: "))
a_price_no_margin = 13
b_price_no_margin = 14
c_price_no_margin = 6

a_price = 15
b_price = 20
c_price = 10

a_name = "Mini chupa chups"
b_name = "Mentos mini chupa chups mix"
c_name = "Sour straps"

def prize_pick(amount):
    if amount < min(a_price,b_price,c_price):
        return ["break"]
    print(f"{amount/100} left")
    def print_and_ask():
        if amount > a_price-1:
            print(f"a: {a_name}: {a_price}")
        if amount > b_price-1:
            print(f"b: {b_name}: {b_price}")
        if amount > c_price-1:
            print(f"c: {c_name}: {c_price}")
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
            
            


if shots == 4:
    max_amount = 100
    player_paid = 2
    money = (shots_in / shots)*max_amount

            
if shots == 10:
    # max_amount = 250
    player_paid = 5
    max_amount = 11
    money = (shots_in / shots)*max_amount
    og_money = money





candy = []
while money > 0.05:
    ret = prize_pick(money)
    if ret[0] == "break":
        break
    if ret[0] == "nanValue":
        continue
    money = money - ret[1]
    candy.append(ret[0])
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
    f.write(f'"{a_name}",') # a name
    f.write(f'"{b_name}",') # b name
    f.write(f'"{c_name}",') # c name
    f.write(f'"{a}",') # How much of a they recieved
    f.write(f'"{b}",') # How much of b they recieved
    f.write(f'"{c}",') # How much of c they recieved
    f.write(f'"{a_price_no_margin / 100}",') # how much each of a cost us
    f.write(f'"{b_price_no_margin / 100}",') # how much each of b cost us
    f.write(f'"{c_price_no_margin / 100}",') # how much each of c cost us
    f.write(f'"{a_price / 100}",') # how much each of a "cost" to the consumers
    f.write(f'"{b_price / 100}",') # how much each of b "cost" to the consumers
    f.write(f'"{c_price / 100}",') # how much each of c "cost" to the consumers
    f.write(f'"{shots}",') # How many shots they bought
    f.write(f'"{shots_in}",') # How many they actually got in
    f.write(f'"{max_amount / 100}",') # What was the max amount they could get
    f.write(f'"{og_money / 100}",') # What did they get to "spend"
    f.write(f'"{(a * a_price_no_margin) + (b * b_price_no_margin) + (c * c_price_no_margin) / 100}",') # how much the candy cost us total
    f.write(f'"{(a * a_price) + (b * b_price) + (c * c_price) / 100}",') # How much the consumers "spent"
    f.write(f'"{player_paid - ((a * a_price) + (b * b_price) + (c * c_price)) / 100}",') # how much we profited
    f.write(f'"{money / 100}",') # how much was left left over from the spree
    f.write(f'\n')
