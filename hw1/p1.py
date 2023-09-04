import numpy as np
import statistics

# Accessing Cholesterol.txt file
data = []
def open_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    data.append(float(line))
                except ValueError:
                    print(f"Skipping non-numeric value: {line}")

def compute_file(file_name):
    open_file(file_name)
    print(file_name)

    # 1. Calculate Mean
    mean = np.mean(data)
    print("Mean: ", mean)

    # 2. Calculate Median
    median = np.median(data)
    print("Median: ", median)

    # 3. Calculate Mode
    mode = statistics.mode(data)
    print("Mode: ", mode)

    # 4. Calculate Range
    range = np.ptp(data)
    print("Range: ", range)

    # 5. Calculate Standard Deviation
    std = np.std(data)
    print("Standard Deviation: ", std)

    # 6. Calculate Variance
    var = np.var(data)
    print("Variance: ", var)

    # 7. Calculate 1st Coefficient of Variation
    cv1 = 3*(mean - median) / std
    print("Coefficient of Variation: ", cv1)

    # 8. Calculate 2nd Coefficient of Variation
    cv2 = sum([(x - mean) ** 3 for x in data]) / (len(data) * std ** 3)
    print("Coefficient of Variation: ", cv2)

compute_file("WEIGHT.txt")