#to github
import random


def uniformIn(lo, hi):
    return random.randrange(lo, hi)


def uniformFloat(lo, hi):
    return random.uniform(lo, hi)


def bernoulli(p=0.5):
    return random.random() < p


def binomial(n, p=0.5):
    heads = 0
    for i in range(n):
        if bernoulli(p):
            heads += 1
    return heads
