from item import Item
from phone import Phone

# item1 = Item("Phone", 100)
item1 = Phone("Apple", 900, 8)



item1.apply_discount()
print(item1.name)
print(item1.price)