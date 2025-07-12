import numpy as np

#Roll one die 1000 times
num_rolls = 500
rolls = np.random.randint(1,7,size=num_rolls)

print(f"First 10 rolls: {rolls[:10]}")

# Count occurence of each number from 1 to 6
values, count = np.unique(rolls, return_counts=True)

print("\n Dice Rolll Frequencies:")
for val, cnt in zip(values, count):
    print(f"{val}: {count} times")

probabilities = count / num_rolls

print("\n Probability of each face (based on simulation):")
for val, prob in zip(values, probabilities):
    print(f"{val}: {float(prob):.3f}")