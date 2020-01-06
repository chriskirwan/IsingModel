import numpy as np
import matplotlib.pyplot as plt
import ising

temps = np.arange(0.1, 5, 0.1)
fields = np.arange(0, 20, 1)
rev_fields = (20,-20,-0.1)
itr = 10
relax = 350
plot_elements = 1


mag_list = []
mag_sus = []

#for f in fields:
#    solve = ising.IsingSolver(1, grid_type='square', dim=20, initial_state='hot', H=f)
#    solve.maglist = []
#    solve.run(num_itr = itr+relax, T=5)
   
#    mag_list.append(np.mean((solve.maglist[relax:])))
#    mag_sus.append((1/5)*np.var((solve.maglist[relax:])))
    
for g in rev_fields:
    solve = ising.IsingSolver(1, grid_type='square', dim=5, initial_state='hot', H=g)
    solve.maglist = []
    solve.run(num_itr = itr+relax, T=1)
   
    mag_list.append(np.mean((solve.maglist[relax:])))
    mag_sus.append((1/5)*np.var((solve.maglist[relax:])))
    
plt.plot(rev_fields, mag_list)