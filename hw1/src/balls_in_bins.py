import numpy as np

def toss(num_ball, num_bin):
    res = np.zeros(num_bin)
    for i in range(num_ball):
        idx = np.random.randint(num_bin)
        res[idx] += 1
    return res

def toss_two(num_ball, num_bin):
    res = np.zeros(num_bin)
    for i in range(num_ball):
        choice = np.random.choice(num_bin, 2)
        tie_break = np.random.randint(2)
        if res[choice[0]] > res[choice[1]] or (res[choice[0]] == res[choice[1]] and tie_break == 0):
            idx = choice[1]
        elif res[choice[1]] > res[choice[0]] or (res[choice[0]] == res[choice[1]] and tie_break == 1):
            idx = choice[0]
        else: assert(False)
        res[idx] += 1
    return res

num_trial = 10
num_ball = 10000
num_bin = 100

toss_result = []
toss_two_result = []

for i in range(num_trial):
    toss_result.append(np.max(toss(num_ball, num_bin)))
    toss_two_result.append(np.max(toss_two(num_ball, num_bin)))
toss_result = np.sort(toss_result)
toss_two_result = np.sort(toss_two_result)
print("Random Toss:")
print("    Expected value of the maximum bin: {}".format(np.mean(toss_result)))
print("    Standard deviation of the maximum bin: {}".format(np.std(toss_result)))
print("    probability of overflowing a bin is <= 10: {}".format(toss_result[num_trial // 10 * 9]))
print("Random Toss with Two Choice:")
print("    Expected value of the maximum bin: {}".format(np.mean(toss_two_result)))
print("    Standard deviation of the maximum bin: {}".format(np.std(toss_two_result)))
print("    probability of overflowing a bin is <= 10: {}".format(toss_two_result[num_trial // 10 * 9]))
