import numpy as np
import matplotlib.pyplot as plt
import ising

temps = np.arange(0.1, 5, 0.1)
itr = 50
relax = 50
plot_elements = 4

a = []
for i in range(plot_elements):
    solve = ising.IsingSolver(1, grid_type='hexagon', dim=20, initial_state='cold')

    
    ene_list = np.zeros(len(temps))
    #heat_cap = np.zeros(len(temps))
    i=0
    for t in temps:
        solve.avenglist = []
        solve.run(num_itr=itr+relax, T=t)
    
        ene_list[i] = np.mean(solve.avenglist[relax:])
        #heat_cap[i] = (1/t**2)*np.var(solve.avenglist[relax:])
        i += 1
    a.append(ene_list)    
    
    
    plt.plot(temps, ene_list, alpha=0.3)

f = np.mean(a, axis=0)
g = np.std(a, axis=0)
plt.plot(temps, f, color='k', label='Average Energy (%d runs)' % plot_elements)
plt.fill_between(temps, f+g,f-g,  color='grey', alpha=0.4)
plt.xlabel('Temperature [Arb. Units]')
plt.ylabel('Average Energy per Site [Arb. Units]')
plt.legend()