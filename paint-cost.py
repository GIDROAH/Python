import math
color = int(input())
color_price = (color * 5.00) + 40.00
total_cost = color_price + (color_price/10)
print(math.ceil(total_cost))