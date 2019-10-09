import random
from collections import Counter
import matplotlib.pyplot as plt

# total of 100 people, generate a friend# for each person
random.seed(10)
num_friends = [int(100*random.random()) for _ in range(100)]

# get the min max
min_val = min(num_friends)
max_val = max(num_friends)
print(f'people with most friends have {max_val} and people with lest friends have {min_val}')

# the histogram will use x axis as number of friends
# y to count the number of friends
friend_counts = Counter(num_friends)
max_count = max(friend_counts.values())
xs = range(101)
ys = [friend_counts[i] for i in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, max_count])
plt.title('Histogram of friend counts')
plt.xlabel('number of friends')
plt.ylabel('count')
plt.show()