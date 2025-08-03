import numpy as np

data = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

average_value = np.mean(data)

print(f"\n Average Temperature:",average_value)

minimum_value = np.min(data)
print(f"Minimum value: {minimum_value}")

maximum_value = np.max(data)
print(f"Maximum value: {maximum_value}")

fahrenheit_temperatures = (data * 9/5) + 32

print(f"Fahrenheit temperatures: {fahrenheit_temperatures}")

indices = np.where(data > 20)
print(indices)