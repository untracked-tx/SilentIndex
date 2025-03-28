import csv
from datetime import datetime

questions = [
    ("Resentment", "How many apologies did you give that weren’t earned?"),
    ("Silence", "How many times did you swallow a correction today?"),
    ("Attention", "How long did you listen without being heard? (minutes)"),
    ("Empathy", "How many emotional supports did you provide without return?")
]

filename = "emotional_ledger.csv"

def log_transaction(category, units, desc):
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), category, units, desc])

print("SilentIndex CLI: Emotional Ledger")

for category, question in questions:
    try:
        response = input(f"{question} ")
        units = float(response)
        log_transaction(category, units, question)
    except:
        print("Skipped or invalid input.")

print(f"Logged to {filename}. No one will see it but you.")
