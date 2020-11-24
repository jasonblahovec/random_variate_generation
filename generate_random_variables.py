import numpy as np
import math

np.set_printoptions(suppress=True)

class generate_uniform():
    def __init__(self, n = 1000, seed = 412, a = 0, b = 1, mult = 16807, mod = (2**31)-1):
        self.n = n
        self.seed = seed
        self.mult = mult
        self.mod = mod
        
        self.a = a 
        self.b = b
        
        self.get_observations()
        
    def get_observations(self):
        self.observations = np.ones(self.n)*self.seed
        for i in range(1,len(self.observations)):
            self.observations[i] = (self.b-self.a)*((self.observations[i-1]*self.mult)%self.mod)/self.b
  
        self.observations = (self.observations/self.mod)
    
class generate_normal():

    def __init__(self, n = 1000, seed = 412, mu = 0, sigma = 1, unif_mult = 16807, unif_mod = (2**31)-1):
        self.n = n
        self.seed = seed
        self.mu = mu
        self.sigma = sigma        
        self.unif_mult = unif_mult
        self.unif_mod = unif_mod
        
        self.get_bm_normals()

    def get_bm_normals(self):
        u1 = generate_uniforms(n = self.n, seed = self.seed, a = 0, b = 1 , mult = self.unif_mult, mod = self.unif_mod)
        u2 = generate_uniforms(n = self.n, seed = self.seed, a = 0, b = 1 , mult = self.unif_mult, mod = self.unif_mod)
        
        self.observations = ((-2*np.log(u1.observations))**.5)*(np.cos(2*np.pi*u2.observations))
 
class generate_bernoulli():

    def __init__(self, n = 1000, seed = 412, p = 0.5, unif_mult = 16807, unif_mod = (2**31)-1):
        self.n = n
        self.seed = seed
        self.p = p
        self.unif_mult = unif_mult
        self.unif_mod = unif_mod
        
        self.get_bernoulli()

    def get_bernoulli(self):
        u1 = generate_uniforms(n = self.n, seed = self.seed, a = 0, b = 1 ,  mult = self.unif_mult, mod = self.unif_mod)
        
        self.observations = np.where(u1.observations > self.p, 0, 1)   
        
class generate_exponential():

    def __init__(self, n = 1000, seed = 412, _lambda = 1, unif_mult = 16807, unif_mod = (2**31)-1):
        self.n = n
        self.seed = seed
        self._lambda = _lambda
        self.unif_mult = unif_mult
        self.unif_mod = unif_mod
        
        self.get_exponential()
        
    def get_exponential(self):
        u1 = generate_uniforms(n = self.n, seed = self.seed, a = 0, b = 1 ,  mult = self.unif_mult, mod = self.unif_mod)
        self.observations = (-1/self._lambda)*np.log(1-u1.observations)
        
class generate_geometric():

    def __init__(self, n = 1000, seed = 412, p = .5, unif_mult = 16807, unif_mod = (2**31)-1):
        self.n = n
        self.seed = seed
        self.p = p
        self.unif_mult = unif_mult
        self.unif_mod = unif_mod
        
        self.get_geometrics()
        
    def get_geometrics(self):
        u1 = generate_uniforms(n = self.n, seed = self.seed, a = 0, b = 1 ,  mult = self.unif_mult, mod = self.unif_mod)
        self.observations = np.ceil(np.log(u1.observations)/np.log(1-self.p))
