# Data Structures
inventory = ["laptop", "mouse", "keyboard"]
inventory.append("monitor")

product_dimensions = (1920, 1080)

product_details = {
    "sku": "TECH-8821",
    "categories": ["electronics", "peripherals"],
    "in_stock": True
}

warehouse_zones = {"Zone-A", "Zone-B", "Zone-A", "Zone-C"}

print(f"Inventory List: {inventory}")
print(f"Product Categories: {product_details['categories']}")
print(f"Unique Warehouse Zones: {warehouse_zones}")

# Functions and Type Hinting
def calculate_tax(subtotal: float, tax_rate: float = 0.08) -> float:
    tax_amount = subtotal * tax_rate
    return subtotal + tax_amount

final_bill = calculate_tax(250.0, 0.05)
print(f"Total Amount after Tax: ${final_bill:.2f}")

# List Comprehension
prices = [12, 45, 80, 110, 210]
discounted_prices = [p * 0.9 for p in prices if p > 50]
print(f"Discounted items over $50: {discounted_prices}")