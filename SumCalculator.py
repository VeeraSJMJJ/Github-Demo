import matplotlib.pyplot as plt

# Step 1: Input
n = int(input("Enter a positive integer n: "))

# Step 2: Initialize variables
total = 0
x_values = []
y_values = []

# Step 3: Loop to calculate cumulative sum
for i in range(1, n + 1):
    total += i
    x_values.append(i)         # Numbers from 1 to n
    y_values.append(total)     # Cumulative sum at each step

# Step 4: Display result
print(f"\nThe sum of numbers from 1 to {n} is: {total}")

# Step 5: 2D Line Chart
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, marker='o', color='green', linestyle='-', linewidth=2)
plt.title(f'Cumulative Sum from 1 to {n}', fontsize=14)
plt.xlabel('Number (i)')
plt.ylabel('Cumulative Sum')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(range(1, n + 1))
plt.tight_layout()
plt.show()
