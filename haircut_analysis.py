hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Calculate total average price of all haircuts

total_price = 0
for price in prices:
    total_price += price

average_price = total_price / len(prices)

# Apply a discount to each haircut price
new_prices = [price - 5 for price in prices]

# Calculate revenue for each hairstyle based on weekly haircut counts
revenues = []
for i in range(len(hairstyles)):
    revenue = prices[i] * last_week[i]
    revenues.append(revenue)

total_revenue = sum(revenues)
average_daily_revenue = total_revenue / 7

# Find hairstyles that cost under $30 after discount
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

# Print results
print("Average Haircut Price:", average_price)
print("Updated Prices After $5 Discount:", new_prices)
print("Total Revenue from Last Week:", total_revenue)
print("Average Daily Revenue:", average_daily_revenue)
print("Haircuts Under $30 After Discount:", cuts_under_30)
