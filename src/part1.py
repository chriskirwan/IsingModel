import numpy as np
import matplotlib.pyplot as plt
import ising

temps = np.arange(0.1, 5, 0.1)
itr = 500
relax = 50

x = np.arange(0, 500, 1)
y = np.arange(0,1,0.1)
plot_elements = 7


plt.figure(1)
a = []
for i in range(plot_elements):
    solve = ising.IsingSolver(1, grid_type='square', dim=20, initial_state='hot', H=0)
    solve.run(num_itr = itr, T=1)
    a.append(np.abs(solve.maglist))
    plt.plot(x, np.abs(solve.maglist), alpha=0.2)

f = np.mean(a, axis=0)
g = np.std(a, axis=0)
plt.plot(x, f, color='k', label='Average Magnetisation (%d runs), $T=1$' % plot_elements)
plt.fill_between(x, f+g,f-g,  color='grey', alpha=0.4)

#plt.title("Steps to Reach Equilibrium for 20x20 lattice")
plt.xlabel("Number of Iterations")
plt.ylabel("Average Magnetisation (Per Spin)")
plt.legend()
