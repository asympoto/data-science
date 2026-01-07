products = [
    {"name": "Phone", "price": 12000},
    {"name": "Laptop", "price": 60000},
    {"name": "Watch", "price": 2500},
    {"name": "Headset", "price": 1500},
    {"name": "Tablet", "price": 18000}
]

premium = [p for p in products if p["price"] > 10000]
print("Premium Products:")
for p in premium:
    print(p)

products.sort(key=lambda x: x["price"])
print("\nSorted by Price:")
for p in products:
    print(p)

unique_prices = {p["price"] for p in products}
print("\nUnique Prices:", unique_prices)

print("\nDiscount Eligibility:")
for p in products:
    if p["price"] > 15000:
        print(p["name"], "→ 20% Discount")
    elif p["price"] > 5000:
        print(p["name"], "→ 10% Discount")
    else:
        print(p["name"], "→ No Discount")
