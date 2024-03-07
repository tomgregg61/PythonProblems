
shopList = {}
prices = []
for i in range(5):
    choice = input("Please enter an item followed by its price: ")
    shop = []
    shop = choice.split()
    if(len(shop) < 3):
        shopList[shop[-1]] = shop[0]
        prices += [shop[-1]]
    else:
        item = ""
        for i in range(len(shop) - 1):
            item += (shop[i]+" ")
        shopList[shop[-1]] = item
        prices += [shop[-1]]
sortedPrices = sorted(prices)

for i in range(len(sortedPrices)):
    print(shopList[sortedPrices[i]], end=" ")
    print(sortedPrices[i])

#Ask if there is a simpler solution and check if space created is a problem
