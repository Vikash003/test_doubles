class Checkout:
    class Discount:
        def __init__(self, noOfItems, disPrice):
            self.noOfItems = noOfItems
            self.disPrice = disPrice

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Bad Item")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(item, cnt)
        return total

    def calculateItemTotal(self, item, cnt):
        itemTotal = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt > discount.noOfItems:
                itemTotal += self.calculateDisItemTotal(item, cnt, discount)
            else:
                itemTotal += self.prices[item] * cnt
        else:
            itemTotal += self.prices[item] * cnt
        return itemTotal

    def addDiscount(self, item, noOfItems, disPrice):
        discount = self.Discount(noOfItems, disPrice)
        self.discounts[item] = discount

    def calculateDisItemTotal(self, item, cnt, discount):
        disItemTotal = 0
        noOfDiscounts = round(cnt/discount.noOfItems)
        disItemTotal += noOfDiscounts * discount.noOfItems * discount.disPrice
        rem = cnt % discount.noOfItems
        disItemTotal += rem * self.prices[item]
        return disItemTotal
