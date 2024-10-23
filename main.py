shots = int(input("Shots 4 or 10:  "))
shots_in = int(input("Amount oif shots in: "))

def prize_pick(amount):
    if amount < 6:
        return ["break"]
    print(f"{amount/100} left")
    def print_and_ask():
        if amount > 12:
            print("a: Mini chupa chups: 0.13")
        if amount > 13:
            print("b: Mentos mini chupa chups mix: 0.14")
        if amount > 5:
            print("c: Sour straps: 0.06")
        x = str(input("enter option: "))
        return x
    x = print_and_ask()
    if x == "a":
        if amount > 12:
            return ["a", 13]
        else:
            print("not enough money!")
            return ["nanValue"]
    if x == "b":
        if amount > 13:
            return ["b", 14]
        else:
            print("not enough money!")
            return ["nanValue"]
    if x == "c":
        if amount > 5:
            return ["c", 6]
        else:
            print("not enough money!")
            return ["nanValue"]
    print("invalid value!")
    return ["nanValue"]
            
            


if shots == 4:
    max_amount = 100
    money = (shots_in / shots)*max_amount

            
if shots == 10:
    max_amount = 250
    # max_amount = 7
    money = (shots_in / shots)*max_amount





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
        
print(f"{a} x mini chupa chups")
print(f"{b} x mentos mini chupa chups mix")
print(f"{c} x SOur straps")

with open("sales.txt", "a") as f:
    if shots == 10:
        paid = 2.5
    else:
        paid = 1
    f.write(f"{(a*0.13) + (b * 0.14) + (c * 0.06)}|||{a} mini chupas, {b} mentos mini chupa chupas mix, {c} sour straps. Consumer paid ${paid}. Candy cost {(a*0.13) + (b * 0.14) + (c * 0.06)}. Total gain: {paid - ((a*0.13) + (b * 0.14) + (c * 0.06))}")
            
