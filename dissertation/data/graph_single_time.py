import fileinput
import matplotlib.pyplot as plt

colors = ['g', 'c', 'r']

# 100
x = []
y50 = []
y90 = []
y99 = []

for line in fileinput.input():
    [vx, vys] = line.split(":")
    [v50, v90, v99] = vys.split(",")
    x.append(int(vx))
    y50.append(int(v50))
    y90.append(int(v90))
    y99.append(int(v99))

assert len(y50) == 10

plt.scatter(x, y50, marker='x', color=colors[0])
plt.scatter(x, y90, marker='o', color=colors[1])
plt.scatter(x, y99, marker='+', color=colors[2])
plt.ylabel("Number of timesteps")
plt.xlabel("Number of cards per offline reader in network")
plt.legend(["50th percentile", "90th percentile", "99th percentile"])

filename = fileinput.filename().split(".")[0] + ".pdf"

plt.savefig("../figures/%s" % filename, format='pdf')
