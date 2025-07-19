def calculate_total_with_tax():
    print("🛒 Calculate total cost of 5 items with tax")

    items = []
    total_cost = 0

    for i in range(1, 6):
        print(f"\nItem {i}:")
        try:
            price = float(input("  Enter base price: ₹ "))
            tax_rate = float(input("  Enter tax % (5, 12, 18, or 24): "))
            if tax_rate not in [5, 12, 18, 24]:
                print("  ❌ Invalid tax rate. Using default 5%.")
                tax_rate = 5.0
        except ValueError:
            print("  ❌ Invalid input. Skipping this item.")
            continue

        tax_amount = price * (tax_rate / 100)
        final_price = price + tax_amount

        items.append({
            "item": i,
            "base_price": price,
            "tax_rate": tax_rate,
            "tax_amount": tax_amount,
            "final_price": final_price
        })

        total_cost += final_price

    print("\n🧾 Itemized Bill:")
    print(f"{'Item':<6}{'Base Price':<12}{'Tax %':<8}{'Tax Amt':<10}{'Final Price':<12}")
    print("-" * 50)
    for item in items:
        print(f"{item['item']:<6}₹{item['base_price']:<11.2f}{item['tax_rate']:<8.2f}₹{item['tax_amount']:<9.2f}₹{item['final_price']:<11.2f}")
    print("-" * 50)
    print(f"{'Total Cost':<34} ₹{total_cost:.2f}")

# Run the function
calculate_total_with_tax()
