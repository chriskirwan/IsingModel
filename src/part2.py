import numpy as np
import matplotlib.pyplot as plt
import ising

temps = np.arange(0.1, 5, 0.1)
itr = 50
relax = 50
plot_elements = 2

def exact_solution(t):  
    return (1 - 1/(np.sinh(2/t)**4))**(1/8)

t_c = 2/np.log(1 + np.sqrt(2))
t_d= 4/np.log(3)
t_f = 2/np.log(2 + np.sqrt(3))
new_temps = np.arange(0.1, t_c, 0.01)
solve = ising.IsingSolver(1, grid_type='hexagon', dim=20, initial_state='cold')

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
plt.axvline(x=t_f)
plt.xlabel("Temperature [Arb. Units]")
plt.ylabel("Susceptibility [Arb. Units]")
plt.legend()
