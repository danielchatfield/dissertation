import fileinput
import matplotlib.pyplot as plt

colors = ['g', 'c', 'r']

# 100
x = []
y50 = []
y90 = []
y99 = []

file = fileinput.input()

header = file.readline()
assert header[0] == "#"
[samples, timesteps, numOffline, _, _, numRevoked] = header[2:].split(',')

samples = int(samples)
timesteps = int(timesteps)
numRevoked = int(numRevoked)
numOffline = int(numOffline)

print "%d samples, %d timesteps" % (samples, timesteps)

x = range(timesteps)
y_cum_naive = [0] * timesteps
y_cum_random = [0] * timesteps

for sample in range(samples):
    line = file.readline()
    assert len(line) > 0 and line[0] == "#"
    for i in range(timesteps):
        line = file.readline()
        assert len(line) > 0 and line[0] != "#"
        [ts, data] = line.split(":")
        [n95, nt, r95, rt] = line.split(",")
        y_cum_naive[i] += int(nt)
        y_cum_random[i] += int(rt)

# normalise
divider = float(samples) * numOffline * numRevoked
y_cum_naive = [y / divider for y in y_cum_naive]
y_cum_random = [y / divider for y in y_cum_random]

assert len(y_cum_naive) == len(y_cum_random)
print len(x) == len(y_cum_naive)

x = x[1:]
y_cum_naive = y_cum_naive[1:]
y_cum_random = y_cum_random[1:]


plt.scatter(x, y_cum_naive, marker='x')
plt.scatter(x, y_cum_random, marker='o')
plt.ylabel("Total propagations of all UIDs")
plt.xlabel("Simulation timesteps elapsed")
plt.legend(["Naive algorithm", "Random algorithm"], loc=4)

ax = plt.gca()
ax.ticklabel_format(useOffset=False)
ax.set_xlim([0, timesteps])
ax.set_ylim([0, 1])
vals = ax.get_yticks()
ax.set_yticklabels(['{:3.0f}%'.format(rv*100) for rv in vals])

filename = fileinput.filename().split(".")[0]
filename = 'crowd_%d_%d' % (numOffline, numRevoked)

plt.savefig("../figures/%s.pdf" % filename, format='pdf')
