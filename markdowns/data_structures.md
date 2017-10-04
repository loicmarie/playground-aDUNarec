# Data structures

Before we begin, we have to decide which "tools" to use. We can think of algorithmic as a card game, in which we'll choose cards to elaborate strategy, and eventually win the game.
Here, our cards are data structures, and because it's hard to play without any card, it is necessary to learn the principles of choosing the right data structure to create an algorithm and
to handle data in the most optimal manner.

## Why is it so important ? I thought a simple list should do the job.

In theory that's right, but the performances of your algorithm will highly depend on this choice. In some cases, a list will be sufficient, in others it will be irrelevant for some reasons. Let's take an exampl:

```python runnable
import time

start_time = time.time()
a = list(range(10**6))
print(10 in a)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
a = set(range(10**6))
print(10 in a)
print("--- %s seconds ---" % (time.time() - start_time))
```
