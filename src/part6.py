import numpy as np
import matplotlib.pyplot as plt
import ising

temps = np.arange(0.1, 5, 0.1)
itr = 10
relax = 50

x = np.arange(0, 500, 1)
y = np.arange(0,1,0.1)
plot_elements = 2


#plt.figure(1)
#a = []
#for i in range(plot_elements):
#    solve = ising.IsingSolver(1, grid_type='square', intr='nextnn',dim=20, initial_state='hot', H=0, J=[1,0.5])
#    solve.run(num_itr = itr, T=1)
#    a.append(np.abs(solve.maglist))
#    plt.plot(x, np.abs(solve.maglist), alpha=0.2)

#f = np.mean(a, axis=0)
#g = np.std(a, axis=0)
#plt.plot(x, f, color='k', label='Average Magnetisation (%d runs), $T=1$' % plot_elements)
#plt.fill_between(x, f+g,f-g,  color='grey', alpha=0.4)

#plt.title("Steps to Reach Equilibrium for 20x20 lattice")
#plt.xlabel("Number of Iterations")
#plt.ylabel("Average Magnetisation (Per Spin)")
#plt.legend()


solve = ising.IsingSolver(1, grid_type='square', intr='nextnn',dim=20, initial_state='cold', H=0, J=[1,70])
a = []
for i in range(plot_elements):
    mag_list = np.zeros(len(temps))
    #mag_sus = np.zeros(len(temps))
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
#plt.plot(new_temps, exact_solution(new_temps))
plt.xlabel("Temperature [Arb. Units]")
plt.ylabel("Spontaneous Magnetisation [Arb. Units]")
plt.legend()