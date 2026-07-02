cost_pr = int(input("enter a cost prize : "))
sell_pr = int(input("enter a sell prize : "))

if sell_pr > cost_pr :
    print("profit ",sell_pr-cost_pr)
elif sell_pr == cost_pr :
    print("no profit no lost ")
else :
    print("loss",cost_pr-sell_pr)       