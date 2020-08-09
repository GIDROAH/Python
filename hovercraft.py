sales = int(input())
hovercraft = 2000000
sell_price = 3000000
factory = 10
insurance = 1000000
total_cost = (hovercraft *factory) + insurance
profit = sell_price * sales
if profit > total_cost:
    print("Profit")
elif profit == total_cost:
    print("Broke Even")
elif profit < total_cost:
    print("Loss")