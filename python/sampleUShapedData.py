import numpy as np

# Parameters for the U-shaped distribution
min_value = 5
max_value = 20
num_samples = 1000  # Number of samples to generate

# Generating U-shaped distribution data
# Create a uniform distribution and transform it into a U-shaped distribution
uniform_data = np.random.uniform(0, 1, num_samples)
u_shaped_data = min_value + (max_value - min_value) * np.minimum(uniform_data, 1 - uniform_data)

# Printing the first 10 samples as an example
print(u_shaped_data[:10])
