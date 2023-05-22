# discount_project

This repository consists of a Python file named "basic_logic.py" that contains the core logic of this Django project.

## Getting Started

### Prerequisites

- Python 3.9
- Django

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/agnelgeo/discount_project.git
   ```

2. Create and activate a virtual environment:

   ```shell
   cd django-project
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```shell
   python manage.py migrate
   ```

5. Start the development server:

   ```shell
   python manage.py runserver
   ```

6. Access the application at `http://localhost:8000` in your web browser.


## Project Description:

This project implements a catalog system with 3 products, namely Product A, Product B, and Product C. Each product has an associated price as listed below:

- Product A: $20
- Product B: $40
- Product C: $50

### Discount Rules

The catalog applies the following discount rules:

1. **Flat 10% Discount**: If the total cart value exceeds $200, a flat $10 discount is applied to the cart total.
2. **Bulk 5% Discount**: If the quantity of any single product exceeds 10 units, a 5% discount is applied to the total price of that product.
3. **Bulk 10% Discount**: If the total quantity of products in the cart exceeds 20 units, a 10% discount is applied to the cart total.
4. **Tiered 50% Discount**: If the total quantity of products exceeds 30 units and any single product quantity is greater than 15, a 50% discount is applied to the products that exceed 15 units. The first 15 units are priced at the original price, while the additional units above 15 receive the 50% discount.

Note: Only one discount rule can be applied per purchase. If multiple discounts are applicable, the program calculates the discount amount for each rule and applies the most beneficial one for the customer.

### Fees

In addition to the product prices and discounts, the catalog also includes the following fees:

- **Gift Wrap Fee**: $1 per unit for each product that is gift-wrapped.
- **Shipping Fee**: Products are packed in packages, with each package accommodating up to 10 units. The shipping fee for each package is $5.

### Program Usage

To use the program, follow these steps:

1. Run the program, which prompts you to enter the quantity of each product you wish to purchase. Additionally, specify whether you want the product to be gift-wrapped.
2. The program will calculate and display the following details:

   - The product name, quantity, and total amount for each selected product.
   - The subtotal of the cart.
   - The discount name applied and the discount amount.
   - The shipping fee and the gift wrap fee.
   - The total amount to be paid.
