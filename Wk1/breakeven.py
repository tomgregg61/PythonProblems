variableCost = 20.0
fixedCosts = 50000.0
salePrice = 40.0
profitPerItem = salePrice - variableCost
breakEven = fixedCosts / profitPerItem

print("Cost to produce each item: {} \nSale price for each item: {} \nFixed costs: {} \nProfit per item: {} \nBreakeven: {} items".format(variableCost, salePrice, fixedCosts, profitPerItem, breakEven))