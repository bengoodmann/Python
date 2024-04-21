import os

auctioneers: dict[str, int] = {}

end_auction = False

while not end_auction:
    name = input("What's your name?\n> ").title()
    bid = int(input("How much do you want to bid\n>$"))
    auctioneers[name] = bid

    res = int(input("Who else wants to bid?(1 for Yes, 0 for No)\n>"))

    if res == 1:
        os.system("cls")
    else:
        end_auction = True


def highest_bidder(hb: dict):
    highest = 0
    for key in hb:
        if hb[key] > highest:
            highest = hb[key]

    print(f"{key} has the highest bid with ${highest}")


highest_bidder(auctioneers)
