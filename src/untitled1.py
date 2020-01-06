import numpy as np
import matplotlib.pyplot as plt
import ising

temps = np.arange(0.1, 5, 0.1)
itr = 100
relax = 50
plot_elements = 4

solve = ising.IsingSolver(1, grid_type='line', dim=30, initial_state='cold', intr='decay', a=10)

a = []
for i in range(plot_elements):
    mag_list = np.zeros(len(temps))
    mag_sus = np.zeros(len(temps))
    i = 0
    
    for t in temps:
        solve.maglist = []
        solve.run(num_itr = itr+relax, T=t)
        
        mag_list[i] = np.mean(np.abs(solve.maglist[relax:]))
        #mag_sus[i] = (1/t)*np.var(np.abs(solve.maglist[relax:]))
        
        i += 1
    
    a.append(mag_list)
    
    plt.plot(temps, mag_list, alpha=0.3)
    #plt.plot(temps, mag_sus, alpha=0.3)

f = np.mean(a, axis=0)
g = np.std(a, axis=0)
plt.plot(temps, f, color='k', label='Average Magnetisation (%d runs)' % plot_elements)
plt.fill_between(temps, f+g,f-g,  color='grey', alpha=0.4)
plt.xlabel("Temperature [Arb. Units]")
plt.ylabel("Spontaneous Magnetisation [Arb. Units]")
plt.legend()