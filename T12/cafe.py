menu = ["milkshake" , "tea" , "muffin" , "water"]
stock = {"milkshake" : 10,
         "tea" : 2,
         "muffin" : 7,
         "water" : 30 }

price = {"milkshake" : 5,
         "tea" : 1,
         "muffin" : 2,
         "water" : 0 }

# for each item in stock and price, multiply the pair with each other

total_stock = [stock[item]*price[item] for item in stock and price]
print(total_stock)

# summing up the total_stock list

print(f"£{sum(total_stock)}")