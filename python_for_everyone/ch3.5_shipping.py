

shippingCost = 0.0
shippingCost_string = str(shippingCost)
countyInput = input("Enter the county: ")
country = countyInput
stateInput = input("Bet, now enter your damn State!: ")
state = stateInput


if (country == "USA" or country == "usa"):
    if(state == "AK" or state == "ak" or state == "HI" or state == "hi"):
        shippingCost == 10.0
    else: shippingCost == 5.0

else: shippingCost = 10.0

# %s = string placeholder
# %.2f = floating number with 2 decimal places
# % (state, country, shippingCost) = values inserted in order into the placeholders
print("Shipping cost to %s, %s: $%.2f" % (state, country, shippingCost))

print("Shipping cost to ", state, ",", country, ":", shippingCost)

print("Shipping cost to " + state + ", " + country + ": $" + shippingCost_string)
