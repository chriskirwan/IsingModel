import numpy as np
import matplotlib.pyplot as plt
import ising

temps = np.arange(0.1, 5, 0.1)
itr = 10
relax = 50

solve = ising.IsingSolver(1, grid_type='square', dim=200, initial_state='hot')
solve.run(num_itr = itr, T=1)
plt.figure(1)
solve.print_system(solve.moments)

