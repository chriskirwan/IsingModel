# IsingModel
## PYU33C01 Project: Computational Simulation of the Ising Model

### Project Structure For IsingSolver()
<br>
Contains the IsingSolver class, which is called using IsingSolver(args)
<br>
The following is a list of the arguments the it takes
<br>
``grid_type``
<br>
    This is the lattice configuration. Takes sting values: line, square, triangle, hexagon, cube. Default is square
<br>
-dim
<br>
    This is the dimension of the lattice. Takes integer values. Default is 100
<br>
-initial_state 
 <br>   
    This is the initial configuration of the lattice. Takes string values: hot, cold. Default is hot
-pbcs 
    Sets the periodic boundary conditions. Takes boolean string: True or False. Default is on.
    In this notebook, the pbcs is set to always be true
-intr 
    Sets the interaction type for each lattice. Takes string values: nn, nextnn, decay. Default is nn
-T 
    Sets the system temperature. Takes float vaules. Default is 1
-J -
    Sets the interaction strenght. Takes list/array values. Default is [1]
-H -
    Sets the magnetic field strength. Takes float values. Default is 0
-a -
    Sets the decay interaction strength. Takes float values above 1. Default is 1. 
    
build_grid_square(initial_state)
    Builds a square lattice with either random [-1,1] values (hot) or all [1] values (cold). Similar functions 
    for line and cube exist as well. Outputs a list of the systems moments (moments) and and array of the moments for plotting
    and calculations (system_array)
    
neighbours(N,M,L, system_array)
    Calcuates the nearest neighbours for each grid_type (depending on the value of pbcs)
    
next_neighbours(N,M,L, system_array)
    Calculates the next nearest neighbours for each grid_type
    
intr_decay(N,M)
    Calculates the deacy interaction strength 
    
square_energy(N,M)
    Calculates the energy at each lattice point (calling the previous 3 functions)
    
internal_energy()
    Calculates the total energy and average energy of the entire grid
    
magnetisation()
    Calculates the average magnetisation
    
single_update(T)
    Runs a single "sweep" through the lattice at a given temperature. This is the routine that performs the MH algorithm
    
run(num_itr, T)
    This function iteratively calls single_update() num_itr number of times. This is the routine that peforms the the statistics gathering
    
print_system(moments)
    Prints the resulting lattice structure.
