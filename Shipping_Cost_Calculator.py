import numpy as np
# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate
empty_list = []
empty_list.append(shipping_cost)
shipping_array = np.array(empty_list)
sorte_array = np.argsort(shipping_array)

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

# Here is a new update by seba7037

# here is another update by Seba7027
## calculating index

print(f" index")
