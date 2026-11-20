import numpy as np
import statistics as Stats

flips = np.random.randint(0, 2, size=10)  # 0 = tails, 1 = heads
print("Chance of heads:", flips.mean())

rng = np.random.default_rng(42)
days = 1000

cloudy = rng.random(days) < 0.5                    # half the days are cloudy
rain = rng.random(days) < np.where(cloudy, 0.6, 0.1)  # cloudy days rain more often

print("Chance of rain overall:", rain.mean())
print("Chance of rain on cloudy days:", rain[cloudy].mean())

rain_probability = 50 # Convert to percentage

if rain_probability < 50:
    print("Rain is unlikely.")
else:
    print("Rain is likely.")


rng = np.random.default_rng(1)
people = 1000

sick = rng.random(people) < 0.01  # 1% of people are sick
test_positive = rng.random(people) < np.where(sick, 0.95, 0.05)  # test is right 95% of the time for sick people, wrong 5% for healthy people

print("Chance a positive test means really sick:", sick[test_positive].mean())

# Range
# Percentile
# Quartile
# variance
# Standard deviation
# outliers
# correlation

data = [5, 2, 7, 8, 5, 6, 9, 1, 4, 5, 3]
print("Mean:", Stats.mean(data))
print("median:", Stats.median(data))
print("Mode:", Stats.mode(data))


