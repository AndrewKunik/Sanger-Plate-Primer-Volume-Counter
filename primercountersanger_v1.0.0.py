from collections import Counter

# Input data (copy-paste from your spreadsheet)
forward_primers = """
2F1_0
2F1_0
2F1_0
2F0_1
2F0_1
2F0_1
1F1_0
1F1_0
1F1_0
1F1_0
1F1_0
1F1_0
2F0_1
2F0_1
2F0_1
"""

reverse_primers = """
2R2_0
2R2_0
2R2_0
2R2_0
2R2_0
2R2_0
1R3_0
1R3_0
1R3_0
1R3_0
1R3_0
1R3_0
2R1_0
2R1_0
2R1_0
"""

# Clean and split the input into lists
forward_list = forward_primers.strip().split("\n")
reverse_list = reverse_primers.strip().split("\n")

# Count primer occurrences using Counter
forward_counts = Counter(forward_list)
reverse_counts = Counter(reverse_list)

# Function to calculate microliters
def calculate_microliters(primer_counts, multiplier=5):
    return {primer: count * multiplier for primer, count in primer_counts.items()}

# Calculate microliters
forward_microliters = calculate_microliters(forward_counts)
reverse_microliters = calculate_microliters(reverse_counts)

# Display results
print("Forward Primers (Microliters):")
for primer, microliters in forward_microliters.items():
    print(f"{primer}: {microliters} µL")

print("\nReverse Primers (Microliters):")
for primer, microliters in reverse_microliters.items():
    print(f"{primer}: {microliters} µL")