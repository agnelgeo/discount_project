import math

# Define product prices
product_a_price = 20
product_b_price = 40
product_c_price = 50

# Get input from user
try:
    product_a_quantity = int(input("Enter quantity of product A (or leave blank for 0): ")) or 0
except ValueError:
    product_a_quantity = 0

try:
    product_b_quantity = int(input("Enter quantity of product B (or leave blank for 0): ")) or 0
except ValueError:
    product_b_quantity = 0

try:
    product_c_quantity = int(input("Enter quantity of product C (or leave blank for 0): ")) or 0
except ValueError:
    product_c_quantity = 0

is_gift_wrapped = input("Is the product gift wrapped? (Y/N): ").lower() == "y"

# Calculate total amount for each product
product_a_total = product_a_price * product_a_quantity
product_b_total = product_b_price * product_b_quantity
product_c_total = product_c_price * product_c_quantity

# Calculate subtotal
subtotal = product_a_total + product_b_total + product_c_total
total_quantity = product_a_quantity + product_b_quantity + product_c_quantity

# Initialize discount values and names
rule_1_discount = 0
rule_2_discount = 0
rule_3_discount = 0
rule_4_discount = 0
discount_name = ""

# Check if cart total exceeds $200 (flat_10_discount)
if subtotal > 200:
    rule_1_discount = 10

# Check for bulk_5_discount
if product_a_quantity > 10:
    rule_2_discount += product_a_total * 0.05

if product_b_quantity > 10:
    rule_2_discount += product_b_total * 0.05

if product_c_quantity > 10:
    rule_2_discount += product_c_total * 0.05

# Check if total quantity exceeds 20 units (bulk_10_discount)
if total_quantity > 20:
    rule_3_discount = subtotal * 0.1

# Check if total quantity exceeds 30 units and any single product quantity greater than 15 (tiered_50_discount)
if total_quantity > 30 and (product_a_quantity > 15 or product_b_quantity > 15 or product_c_quantity > 15):
    if product_a_quantity > 15:
        rule_4_discount += product_a_price * (product_a_quantity - 15) * 0.5

    if product_b_quantity > 15:
        rule_4_discount += product_b_price * (product_b_quantity - 15) * 0.5

    if product_c_quantity > 15:
        rule_4_discount += product_c_price * (product_c_quantity - 15) * 0.5

# Determine the highest discount rule
max_discount = max(rule_1_discount, rule_2_discount, rule_3_discount, rule_4_discount)

# Assign the discount name based on the highest discount rule
if max_discount == 0:
    discount_name = "No discounts applied"
elif max_discount == rule_1_discount:
    discount_name = "flat_10_discount"
elif max_discount == rule_2_discount:
    discount_name = "bulk_5_discount"
elif max_discount == rule_3_discount:
    discount_name = "bulk_10_discount"
elif max_discount == rule_4_discount:
    discount_name = "tiered_50_discount"

# Calculate gift wrap fee
gift_wrap_fee = (product_a_quantity + product_b_quantity + product_c_quantity) * is_gift_wrapped

# Calculate shipping fee
shipping_fee = math.ceil(total_quantity / 10) * 5

# Calculate total amount after discounts and fees
total_amount = subtotal - max_discount + gift_wrap_fee + shipping_fee

# Print the results
print()
print(f"Product A , Quantity:{product_a_quantity } , Total:{product_a_total}")
print(f"Product B , Quantity:{product_b_quantity } , Total:{product_b_total}")
print(f"Product C , Quantity:{product_c_quantity } , Total:{product_c_total}")
print()
print("Subtotal:", subtotal)
print()
print("Discount Applied:", max_discount)
print("Discount Name:", discount_name)
print()
print("Gift Wrap Fee:", gift_wrap_fee)
print("Shipping Fee:", shipping_fee)
print()
print("Total Amount:", total_amount)
