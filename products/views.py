from django.shortcuts import render
from .models import Product
import math

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})



def calculate_order(request):
    if request.method == 'POST':
        
        total_quantity = 0
        subtotal = 0

        product_a_price = 20
        product_b_price = 40
        product_c_price = 50

        product_a_quantity = request.POST.get("quantity_product_1")
        product_a_quantity = int(product_a_quantity) if product_a_quantity is not None else 0

        product_b_quantity = request.POST.get("quantity_product_2")
        product_b_quantity = int(product_b_quantity) if product_b_quantity is not None else 0

        product_c_quantity = request.POST.get("quantity_product_3")
        product_c_quantity = int(product_c_quantity) if product_c_quantity is not None else 0

        is_gift_wrapped = request.POST.get("gift_wrap") == "on"

        product_a_total = product_a_price * product_a_quantity
        product_b_total = product_b_price * product_b_quantity
        product_c_total = product_c_price * product_c_quantity

        subtotal = product_a_total + product_b_total + product_c_total
        total_quantity = product_a_quantity + product_b_quantity + product_c_quantity

        rule_1_discount = 0
        rule_2_discount = 0
        rule_3_discount = 0
        rule_4_discount = 0
        discount_name = ""

        if subtotal > 200:
            rule_1_discount = 10

        if product_a_quantity > 10:
            rule_2_discount += product_a_total * 0.05

        if product_b_quantity > 10:
            rule_2_discount += product_b_total * 0.05

        if product_c_quantity > 10:
            rule_2_discount += product_c_total * 0.05

        if total_quantity > 20:
            rule_3_discount = subtotal * 0.1

        if total_quantity > 30 and (product_a_quantity > 15 or product_b_quantity > 15 or product_c_quantity > 15):
            if product_a_quantity > 15:
                rule_4_discount += product_a_price * (product_a_quantity - 15) * 0.5

            if product_b_quantity > 15:
                rule_4_discount += product_b_price * (product_b_quantity - 15) * 0.5

            if product_c_quantity > 15:
                rule_4_discount += product_c_price * (product_c_quantity - 15) * 0.5

        max_discount = max(rule_1_discount, rule_2_discount, rule_3_discount, rule_4_discount)

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

        gift_wrap_fee = (product_a_quantity + product_b_quantity + product_c_quantity) * is_gift_wrapped
        shipping_fee = math.ceil(total_quantity / 10) * 5
        total_amount = subtotal - max_discount + gift_wrap_fee + shipping_fee

        return render(
            request,
            'order_summary.html',
            {
                'product_info': {
                    'Product A': {"quantity":product_a_quantity,"price":product_a_total},
                    'Product B': {"quantity":product_b_quantity,"price":product_b_total},
                    'Product C': {"quantity":product_c_quantity,"price":product_c_total},
                },
                'subtotal': subtotal,
                'applied_discount': discount_name,
                'discount_amount': max_discount,
                'shipping_total': shipping_fee,
                'gift_wrap_total': gift_wrap_fee,
                'total': total_amount,
            }
        )

    return render(request, 'product_list.html', {'products': Product.objects.all()})
