import random

# random() returns a random floating point number in the range [0.0, 1.0)
print(random.random())

# randint(a, b) returns a random integer N in the range [a, b] including both end points
print(random.randint(1, 10))

# normalvariate(mu, sigma) returns a random floating point number N with mean mu and standard deviation sigma
print(random.normalvariate(0, 1))

# choice(seq) returns a random element from the non-empty sequence seq
print(random.choice([1, 2, 3, 4]))

# sample(population, k) returns a list of k unique elements chosen from the population sequence
print(random.sample([1, 2, 3, 4, 5], k=3))

# shuffle(seq) shuffles the sequence seq in place
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)

# secrets module, true random numbers
import secrets

# secrets.randbelow(n) returns a random integer N in the range [0, n)
print(secrets.randbelow(10))

# secrets.randbits(k) returns an integer with k random bits
print(secrets.randbits(8))
