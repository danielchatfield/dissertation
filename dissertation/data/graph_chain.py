import fileinput
import matplotlib.pyplot as plt

colors = ['g', 'c', 'r']

file = fileinput.input()

header = file.readline()
assert header[:8] == "# chain:"
vals = header[8:].split(',')
vals = vals[0:3] + vals[5:]
vals = [int(x) for x in vals]
[samples, timesteps, numOffline, existing, new] = vals

print "%d samples, %d timesteps" % (samples, timesteps)

x = range(timesteps)
y_cum_naive = [0] * timesteps
y_cum_random = [0] * timesteps
y_cum_skewed = [0] * timesteps

for sample in range(samples):
    line = file.readline()
    assert len(line) > 0 and line[0] == "#"
    for i in range(timesteps):
        line = file.readline()
        assert len(line) > 0
        assert line[0] != "#"
        [ts, data] = line.split(":")
        [nt, rt, st] = data.split(",")
        y_cum_naive[i] += int(nt)
        y_cum_random[i] += int(rt)
        y_cum_skewed[i] += int(st)

# normalise
divider = float(samples) * numOffline * new
y_cum_naive = [y / divider for y in y_cum_naive]
y_cum_random = [y / divider for y in y_cum_random]
y_cum_skewed = [y / divider for y in y_cum_skewed]

assert len(y_cum_naive) == len(y_cum_random)
assert len(x) == len(y_cum_skewed)

x = x[1:]
y_cum_naive = y_cum_naive[1:]
y_cum_random = y_cum_random[1:]
y_cum_skewed = y_cum_skewed[1:]


plt.scatter(x, y_cum_naive, marker='x')
plt.scatter(x, y_cum_random, marker='o')
plt.scatter(x, y_cum_skewed, marker='.', color='r')
plt.ylabel("Total propagations of recent UIDs")
plt.xlabel("Simulation timesteps elapsed")
plt.legend(["Naive", "Random", "Skewed Random"], loc=4)

ax = plt.gca()
ax.ticklabel_format(useOffset=False)
ax.set_xlim([0, timesteps])
ax.set_ylim([0, 1])
vals = ax.get_yticks()
ax.set_yticklabels(['{:3.0f}%'.format(rv*100) for rv in vals])

filename = fileinput.filename().split(".")[0]
filename = 'chain_%d_%d_%d' % (numOffline, existing, new)

plt.savefig("../figures/%s.pdf" % filename, format='pdf')
