import time
import random

currencies = {
    "empathy_credit": 100.0,
    "guilt_pressure": 50.0,
    "presence_drain": 80.0,
    "silence_leverage": 70.0
}

print("SilentIndex SIM: Running value drift model... (CTRL+C to exit)")

try:
    while True:
        for key in currencies:
            drift = random.uniform(-2.0, 2.0)
            currencies[key] += drift
            currencies[key] = round(currencies[key], 2)
        print(f"--- {time.strftime('%H:%M:%S')} ---")
        for k, v in currencies.items():
            print(f"{k}: {v}")
        print()
        time.sleep(3)
except KeyboardInterrupt:
    print("Simulation terminated.")
