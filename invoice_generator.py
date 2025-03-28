import random

categories = [
    "withheld honesty",
    "tolerated imbalance",
    "emotional debt",
    "deferred confrontation",
    "unspoken care"
]

print("SilentIndex GHOST: Generating emotional invoice...\n")

for item in random.sample(categories, 3):
    units = round(random.uniform(1.0, 5.0), 1)
    print(f"- {units} units of {item}")

print("\nTotal cost: future friction")
print("Recommended payment: silence\n")
