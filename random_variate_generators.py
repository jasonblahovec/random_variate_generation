import numpy as np
import math

np.set_printoptions(suppress=True)

class generate_bernoulli():

    def __init__(self, n = 1000, seed = 412, p = 0.5, unif_mult = 16807, unif_mod = (2**31)-1):
        self.n = n
        self.seed = seed
        self.p = p
        self.unif_mult = unif_mult
        self.unif_mod = unif_mod
        
        self.get_bernoulli()

    def get_bernoulli(self):
        u1 = generate_uniform(n = self.n, seed = self.seed, a = 0, b = 1 ,  mult = self.unif_mult, mod = self.unif_mod)
        
        self.observations = np.where(u1.observations > self.p, 0, 1)   

class generate_binomial():
    
    def __init__(self, n = 1000, seed = 412, _trials = 10, _p = .5, mult = 16807, mod = (2**31)-1):
        self.n = n
        self.seed = seed
        self.mult = mult
        self.mod = mod
        
        self.trials = _trials
        self.p = _p
        
        self.get_observations()
    
    def get_observations(self):
        uniforms = np.resize(generate_uniform(n = self.n*self.trials, seed = self.seed, mult = self.mult, mod = self.mod).observations,[self.n,self.trials])
        self.observations = np.sum(np.array([[1 if flip < self.p else 0 for flip in u] for u in uniforms]),axis = 1)
        
class generate_erlang():
    def __init__(self, n = 1000, seed = 412, rate = .5, k = 2, mult = 16807, mod = (2**31)-1):
        self.n = n
        self.seed = seed
        self.mult = mult
        self.mod = mod
        
        self.rate = rate
        self.k = k
        
        self.get_observations()
        
    def get_observations(self):
        self.observations = np.ones(self.n)*self.seed
        expos = generate_exponential(self.k*self.n, self.seed, self.rate, self.mult, self.mod)
        expo_array = []
        for i in range(0,self.k):
            expo_array.append(expos.observations[i*self.n:((i+1)*self.n)])
        self.observations = np.sum(np.array(expo_array).transpose(),axis = 1)

class generate_exponential():

    def __init__(self, n = 1000, seed = 412, _lambda = 1, unif_mult = 16807, unif_mod = (2**31)-1):
        self.n = n
        self.seed = seed
        self._lambda = _lambda
        self.unif_mult = unif_mult
        self.unif_mod = unif_mod
        
        self.get_exponential()
        
    def get_exponential(self):
        u1 = generate_uniform(n = self.n, seed = self.seed, a = 0, b = 1 ,  mult = self.unif_mult, mod = self.unif_mod)
        self.observations = (-1/self._lambda)*np.log(1-u1.observations)

class generate_gamma():
    def __init__(self, n = 1000, seed = 412, rate = 1, k = 1, mult = 16807, mod = (2**31)-1):
        self.n = n
        self.seed = seed
        self.mult = mult
        self.mod = mod
        
        self.rate = rate
        self.k = k
        
        self.get_observations()

    def get_observations(self):
        self.observations = np.ones([self.n,self.k])
        unifs = generate_uniform(n = self.n*self.k, seed = self.seed, a = 0, b = 1, mult = self.mult, mod = self.mod).observations
        self.observations = np.sum(-1*np.log(np.resize(unifs,[self.n, self.k]))/self.rate, axis = 1)
        
class generate_geometric():

    def __init__(self, n = 1000, seed = 412, p = .5, unif_mult = 16807, unif_mod = (2**31)-1):
        self.n = n
        self.seed = seed
        self.p = p
        self.unif_mult = unif_mult
        self.unif_mod = unif_mod
        
        self.get_geometrics()
        
    def get_geometrics(self):
        u1 = generate_uniform(n = self.n, seed = self.seed, a = 0, b = 1 ,  mult = self.unif_mult, mod = self.unif_mod)
        self.observations = np.ceil(np.log(u1.observations)/np.log(1-self.p))        
        
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
        u = generate_uniform(n = 2*self.n, seed = self.seed, a = 0, b = 1 , mult = self.unif_mult, mod = self.unif_mod)
        u1 = u.observations[0:self.n]
        u2 = u.observations[self.n:]
        
        self.observations = (((-2*np.log(u1))**.5)*(np.cos(2*np.pi*u2))*(self.sigma**2))+ self.mu

class generate_triangular():
    
    def __init__(self, n = 1000, seed = 412, a = 0, b = .5, c = 1, mult = 16807, mod = (2**31)-1):
        self.n = n
        self.seed = seed
        self.mult = mult
        self.mod = mod
        
        self.a = a
        self.b = b
        self.c = c
        
        self.uniform_c = (self.c - self.a)/(self.b-self.a)
        
        
        self.get_observations()
    
    def get_observations(self):
        uniforms = generate_uniform(n = self.n, seed = self.seed, mult = self.mult, mod = self.mod).observations
        self.observations = [self.a + ((self.b - self.a) * ((self.uniform_c*u)**.5)) if u <self.uniform_c else self.a + ((self.b - self.a) *(1-((1-self.uniform_c)*(1-u))**.5)) for u in uniforms]

        
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
            self.observations[i] = ((self.observations[i-1]*self.mult)%self.mod)
  
        self.observations = ((self.b-self.a)*(self.observations/self.mod)) + self.a
    
class generate_weibull():
    
    def __init__(self, n = 1000, seed = 412, _shape = 1, _scale = 1, mult = 16807, mod = (2**31)-1):
        self.n = n
        self.seed = seed
        self.mult = mult
        self.mod = mod
        
        self.shape = _shape
        self.scale = _scale
        
        self.get_observations()
    
    def get_observations(self):
        uniforms = generate_uniform(n = self.n, seed = self.seed, mult = self.mult, mod = self.mod).observations
        self.observations = [((-1*np.log((1-u)))**(1/self.shape))*self.scale for u in uniforms]
       
        
