def calc_total(prices, tax):
    # Convert the tax percentage to a decimal
    tax_decimal = float(tax.strip('%')) / 100

    # Calculate the subtotal by summing all prices
    subtotal = sum(prices)

    # Calculate the tax amount
    tax_amount = subtotal * tax_decimal

    # Calculate the total amount including tax
    total = subtotal + tax_amount

    # Format the total as a currency string
    formatted_total = "${:,.2f}".format(total)

    return formatted_total


# Example usage
array = [2.00, 4.00, 4.00]
tax = "10%"
result = calc_total(array, tax)
print(result)