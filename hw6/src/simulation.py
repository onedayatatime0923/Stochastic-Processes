import numpy as np
import matplotlib
import matplotlib.pyplot as plt

m = 100
n = 20
def expr():
    test = np.zeros(n)
    res = np.random.randint(n, size=m)
    for i in range(m):
        test[res[i]] += 1
    return np.sum(test>=15) > 0

trial = 10000
c = 0
for t in range(trial):
    res = expr()
    if res:
        c += 1

print(c / trial)
