import numpy as np

flips = np.random.randint(0, 2, size=1000)  # 0 = tails, 1 = heads
print("Chance of heads:", flips.mean())