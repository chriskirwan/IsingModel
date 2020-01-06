import numpy as np
import matplotlib.pyplot as plt

class IsingSolver():
    
    def __init__(self, temperature, pbcs = True ,intr='nn', grid_type='square' ,initial_state='hot', dim = 100, J=[1], H=0, a=2):
        self.grid_type = grid_type
        self.dim = dim
        self.pbcs = pbcs
        self.T = temperature
        self.J = J
        self.H = H
        self.a = a
        self.intr = intr
        
        
        if self.grid_type == 'square':
            self.build_grid_square(initial_state)
            
        if self.grid_type == 'line':
            self.build_grid_line(initial_state)
            
        if self.grid_type == 'triangle':
            self.build_grid_square(initial_state)
            
        if self.grid_type == 'hexagon':
            self.build_grid_square(initial_state)
        
        if self.grid_type == 'cube':
            self.build_grid_cube(initial_state)
        
        self.maglist = []
        self.maglist_squared = []
        self.energylist = []
        self.avenglist = []
        self.current_energy = self.internal_energy()

    def build_grid_square(self, initial_state):
        ''' This produces either a random square lattice'''
        if initial_state == 'hot':
            system = np.random.choice([-1,1], size = self.dim*self.dim)
        elif initial_state == 'cold': 
            system = np.ones(self.dim*self.dim)
            
        x,y = np.linspace(0, self.dim-1, self.dim), np.linspace(0, self.dim-1, self.dim)
        Y,X = np.meshgrid(y,x)
        self.X, self.Y = X.flatten(), Y.flatten()    
        self.system = system
        self.moments = np.copy(self.system)
        self.system_array = self.moments.reshape(self.dim, -1).T
        
    def build_grid_line(self, initial_state):
        '''This produces either a random 1-D lattice or '''
        if initial_state == 'hot':
            system = np.random.choice([-1,1], size = self.dim)
        elif initial_state == 'cold':
            system = np.ones(self.dim)
        
        x,y = np.linspace(0, self.dim-1, self.dim), 0
        Y,X = np.meshgrid(y,x)
        self.X, self.Y = X.flatten(), Y.flatten()    
        self.system = system
        self.moments = np.copy(self.system)
        self.system_array = np.copy(self.system)
        
    def build_grid_cube(self, initial_state):
        '''This produces a random cube lattice '''
        if initial_state == 'hot':
            system = np.random.choice([-1,1], size = self.dim*self.dim*self.dim)
        elif initial_state == 'cold':
            system = np.ones(self.dim*self.dim*self.dim)
            
        x,y,z = np.linspace(0, self.dim-1, self.dim), np.linspace(0, self.dim-1, self.dim), np.linspace(0, self.dim-1, self.dim)
        Z,Y,X = np.meshgrid(z,y,x)
        self.X, self.Y, self.Z = X.flatten(), Y.flatten(), Z.flatten()
        self.system = system
        self.moments = np.copy(self.system)
        self.systems_array = self.moments.reshape(self.dim, -1).T


    def neighbours(self, N, M, L, system_array):
        a = 0
        
        if self.grid_type == 'line':
            left = ((N-1)%self.dim)
            right = ((N+1)%self.dim)
            
            a = [self.system_array[left], self.system_array[right]]
        
        if self.grid_type == 'square':
                left   = ((N-1) %self.dim, M)
                right  = ((N+1) %self.dim, M)
                top    = (N, (M+1) %self.dim)
                bottom = (N, (M-1) %self.dim)
    
                a = [self.system_array[left[0], left[1]], 
                     self.system_array[right[0], right[1]], 
                     self.system_array[top[0], top[1]], 
                     self.system_array[bottom[0], bottom[1]]]
        
        if self.grid_type == 'hexagon':
            right = ((N+1) %self.dim, M)
            top = (N,(M+1) %self.dim)
            bottom = (N,(M-1) %self.dim)     
            
            a =[self.system_array[right[0],right[1]],
                self.system_array[top[0], top[1]],
                self.system_array[bottom[0], bottom[1]]]
            
        if self.grid_type == 'triangle':
            left   = ((N-1) %self.dim, M)
            right  = ((N+1) %self.dim, M)
            top    = (N, (M+1) %self.dim)
            bottom = (N, (M-1) %self.dim)
            corner1  = ((N-1)%self.dim, (M+1)%self.dim)
            corner2 = ((N-1)%self.dim, (M-1)%self.dim)
            
            a = [self.system_array[left[0], left[1]], 
                 self.system_array[right[0], right[1]], 
                 self.system_array[top[0], top[1]], 
                 self.system_array[bottom[0], bottom[1]], 
                 self.system_array[corner1[0], corner1[1]], 
                 self.system_array[corner2[0], corner2[1]]]
            
        if self.grid_type == 'cube':
            left = ((N-1)%self.dim, M, L)
            right = ((N+1)%self.dim, M, L)
            top = (N, (M+1)%self.dim, L)
            bottom = (N, (M-1)%self.dim, L)
            up = (N, M, (L+1)%self.dim)
            down = (N, M, (L-1)%self.dim)
            
            a = [self.systems_array[left[0], left[1], left[2]], 
                 self.systems_array[right[0],right[1],right[2]],
                 self.systems_array[top[0], top[1], top[2]],
                 self.systems_array[bottom[0], bottom[1], bottom[2]],
                 self.systems_array[up[0], up[1], up[2]],
                 self.systems_array[down[0], down[1], down[2]]]
        return a 

    def next_neighbours(self, N, M, L, system_array):
        a=0
        if self.intr == 'nextnn':
            if self.grid_type == 'square':
                corner1 = ((N-1) %self.dim,(M+1)%self.dim)
                corner2 = ((N-1) %self.dim,(M-1)%self.dim)
                corner3 = ((N+1) %self.dim,(M-1)%self.dim)
                corner4 = ((N+1) %self.dim,(M+1)%self.dim)
                
                a = [self.system_array[corner1[0], corner1[1]],
                     self.system_array[corner2[0], corner2[1]],
                     self.system_array[corner3[0], corner3[1]],
                     self.system_array[corner4[0], corner4[1]]]
        return a
    
    def intr_decay(self, N, M):
        if N == M:
            dist = 100000
        elif N != M:   
            dist = (1/((np.abs(N-M))**self.a))
        
        return dist
    
    def square_energy(self, N, M):
        ''' Calculates energy of spin interaction at site [N, M]'''
        a = 0
        
        if self.intr == 'nn':
            if self.grid_type == 'square' or self.grid_type == 'triangle' or self.grid_type == 'hexagon':
                a = -2*self.J[0]*self.system_array[N,M]*(np.sum(self.neighbours(N,M,0,self.system_array))) - self.H*self.system_array[N,M]
            
            if self.grid_type == 'line':
                a = -2*self.J[0]*self.system_array[N]*(np.sum(self.neighbours(N,0,0,self.system_array)))
            
            if self.grid_type == 'cube':
                a = -2*self.J[0]*self.systems_array[N,M]*(np.sum(self.neighbours(N,M,self.systems_array)))
                
        if self.intr == 'nextnn':
            a = -2*self.J[0]*self.system_array[N,M]*(np.sum(self.neighbours(N,M,0,self.system_array))) 
            - 2*self.J[1]*self.system_array[N,M]*(np.sum(self.next_neighbours(N,M,0,self.system_array))) 
            
        if self.intr == 'decay':
            if self.grid_type == 'line':
                a = -2*self.intr_decay(N,M)*self.system_array[N]
        return a
    
    def internal_energy(self):
        e=0; E=0; E_2=0;
        for i in range(self.dim):
            for j in range(self.dim):   
                e = 0.5*self.square_energy(i,j)
                E += e
                E_2 += e**2

            U = 0.5*(1/self.dim**2)*E

        return U 
    
    def magnetisation(self):
        '''Find the overall magnetization of the system'''
        return (np.mean(self.moments))
    
    def single_update(self, T):
        
        newE = self.current_energy
        
        if self.grid_type == 'line':
            for i in range(self.dim):
                deltaE = -self.J[0]*self.square_energy(i,0)
                if deltaE <= 0:
                    newE += deltaE
                    self.system_array[i]*=-1
                        
                elif np.exp(-deltaE/(self.T)) > np.random.rand():
                    self.system_array[i]*=-1
        
        if self.grid_type == 'square' or self.grid_type == 'triangle' or self.grid_type == 'hexagon':
            for i in range(self.dim):
                for j in range(self.dim):
                    deltaE = -self.J[0]*self.square_energy(i,j)
                    
                    if deltaE <= 0:
                        newE += deltaE
                        self.system_array[i,j]*=-1
                        
                    elif np.exp(-deltaE/(self.T)) > np.random.rand():
                        self.system_array[i,j]*=-1
                
        self.moments = self.system_array.flatten()
        self.maglist.append(self.magnetisation())
        self.maglist_squared.append(self.magnetisation()**2)
        self.energylist.append(newE)
        self.avenglist.append(self.internal_energy())
    
    def run(self, num_itr=100, T=-1):    
        if T != -1:
            self.T=T
            
        for i in range(num_itr):
            self.single_update(T)
                
    def print_system(self, moments):
        plt.scatter(self.X, self.Y, c=self.moments, s=200/self.dim)
        ax = plt.gca()
        ax.set_ylim(ax.get_ylim()[::-1])
