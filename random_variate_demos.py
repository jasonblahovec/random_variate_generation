import random_variate_generators as rv
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams.update({'font.size': 28})

class demo_bernoulli:
    
    def __init__(self,_n,_p):
        n_1 = _n
        n_2 = 2*n_1
        n_3 = 2*n_2

        u_n1   = rv.generate_bernoulli(n = n_1  , seed = 412, p = _p, unif_mult = 16807, unif_mod = (2**31)-1)
        u_n2  = rv.generate_bernoulli(n = n_2 , seed = 412  , p = _p, unif_mult = 16807, unif_mod = (2**31)-1)
        u_n3 = rv.generate_bernoulli(n = n_3, seed = 412    , p = _p, unif_mult = 16807, unif_mod = (2**31)-1)

        print([np.mean(u_n1.observations), np.std(u_n1.observations)])
        print([np.mean(u_n2.observations), np.std(u_n2.observations)])
        print([np.mean(u_n3.observations), np.std(u_n3.observations)])

class demo_binomial():
    
    def __init__(self,_n,_trials,_p):
        n_1 = _n
        n_2 = 2*n_1
        n_3 = 2*n_2

        u_n1   = rv.generate_binomial(n = n_1  , seed = 412, _trials = _trials, _p = .5, mult = 16807, mod = (2**31)-1)
        u_n2  = rv.generate_binomial(n = n_2 , seed = 412, _trials = _trials, _p = .5, mult = 16807, mod = (2**31)-1)
        u_n3 = rv.generate_binomial(n = n_3, seed = 412, _trials = _trials, _p = .5, mult = 16807, mod = (2**31)-1)

        fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False,figsize=(55,20))

        axs[0].hist(u_n1.observations, bins=5)
        axs[1].hist(u_n2.observations, bins=10)
        axs[2].hist(u_n3.observations, bins=20)

        axs[0].set_title('Binomial Results, n = ' + str(n_1), fontsize = 45)
        axs[0].set_xlabel('observed value', fontsize = 45)
        axs[0].set_ylabel('frequency', fontsize = 45)


        axs[1].set_title('Binomial Results, n = '+ str(n_2), fontsize = 45)
        axs[1].set_xlabel('observed value', fontsize = 45)
        axs[1].set_ylabel('frequency', fontsize = 45)

        axs[2].set_title('Binomial Results, n = '+ str(n_3), fontsize = 45)
        axs[2].set_xlabel('observed value', fontsize = 45)
        axs[2].set_ylabel('frequency', fontsize = 45)
        
        plt.savefig("binomial.png")
        print([np.mean(u_n1.observations), np.std(u_n1.observations)])
        print([np.mean(u_n2.observations), np.std(u_n2.observations)])
        print([np.mean(u_n3.observations), np.std(u_n3.observations)])
        
class demo_erlang:
    
    def __init__(self,_n,_rate, _k):
        n_1 = _n
        n_2 = 2*n_1
        n_3 = 2*n_2

        u_n1   = rv.generate_erlang(n = n_1  , seed = 412, rate = _rate, k = _k, mult = 16807, mod = (2**31)-1)
        u_n2  = rv.generate_erlang(n = n_2 , seed = 412  , rate = _rate, k = _k, mult = 16807, mod = (2**31)-1)
        u_n3 = rv.generate_erlang(n = n_3, seed = 412    , rate = _rate, k = _k, mult = 16807, mod = (2**31)-1)

        fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False,figsize=(55,20))

        axs[0].hist(u_n1.observations, bins=10)
        axs[1].hist(u_n2.observations, bins=20)
        axs[2].hist(u_n3.observations, bins=40)

        axs[0].set_title('Erlang Results, n = ' + str(n_1), fontsize = 45)
        axs[0].set_xlabel('observed value', fontsize = 45)
        axs[0].set_ylabel('frequency', fontsize = 45)


        axs[1].set_title('Erlang Results, n = '+ str(n_2), fontsize = 45)
        axs[1].set_xlabel('observed value', fontsize = 45)
        axs[1].set_ylabel('frequency', fontsize = 45)

        axs[2].set_title('Erlang Results, n = '+ str(n_3), fontsize = 45)
        axs[2].set_xlabel('observed value', fontsize = 45)
        axs[2].set_ylabel('frequency', fontsize = 45)
        
        plt.savefig("erlang.png")
        print([np.mean(u_n1.observations), np.std(u_n1.observations)])
        print([np.mean(u_n2.observations), np.std(u_n2.observations)])
        print([np.mean(u_n3.observations), np.std(u_n3.observations)])
        
        
class demo_exponential:
    
    def __init__(self,_n,__lambda):
        n_1 = _n
        n_2 = 2*n_1
        n_3 = 2*n_2

        u_n1   = rv.generate_exponential(n = n_1  , seed = 412, _lambda = __lambda, unif_mult = 16807, unif_mod = (2**31)-1)
        u_n2  = rv.generate_exponential(n = n_2 , seed = 412  , _lambda = __lambda, unif_mult = 16807, unif_mod = (2**31)-1)
        u_n3 = rv.generate_exponential(n = n_3, seed = 412    , _lambda = __lambda, unif_mult = 16807, unif_mod = (2**31)-1)

        fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False,figsize=(55,20))

        axs[0].hist(u_n1.observations, bins=5)
        axs[1].hist(u_n2.observations, bins=10)
        axs[2].hist(u_n3.observations, bins=20)

        axs[0].set_title('Exponential Results, n = ' + str(n_1), fontsize = 45)
        axs[0].set_xlabel('observed value', fontsize = 45)
        axs[0].set_ylabel('frequency', fontsize = 45)


        axs[1].set_title('Exponential Results, n = '+ str(n_2), fontsize = 45)
        axs[1].set_xlabel('observed value', fontsize = 45)
        axs[1].set_ylabel('frequency', fontsize = 45)

        axs[2].set_title('Exponential Results, n = '+ str(n_3), fontsize = 45)
        axs[2].set_xlabel('observed value', fontsize = 45)
        axs[2].set_ylabel('frequency', fontsize = 45)
        
        plt.savefig("exponential.png")
        print([np.mean(u_n1.observations), np.std(u_n1.observations)])
        print([np.mean(u_n2.observations), np.std(u_n2.observations)])
        print([np.mean(u_n3.observations), np.std(u_n3.observations)])

class demo_gamma:
    
    def __init__(self,_n,_rate, _k):
        n_1 = _n
        n_2 = 2*n_1
        n_3 = 2*n_2

        u_n1   = rv.generate_gamma(n = n_1  , seed = 412, rate = _rate, k = _k, mult = 16807, mod = (2**31)-1)
        u_n2  = rv.generate_gamma(n = n_2 , seed = 412  , rate = _rate, k = _k, mult = 16807, mod = (2**31)-1)
        u_n3 = rv.generate_gamma(n = n_3, seed = 412    , rate = _rate, k = _k, mult = 16807, mod = (2**31)-1)

        fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False,figsize=(55,20))

        axs[0].hist(u_n1.observations, bins=10)
        axs[1].hist(u_n2.observations, bins=20)
        axs[2].hist(u_n3.observations, bins=40)

        axs[0].set_title('Gamma Results, n = ' + str(n_1), fontsize = 45)
        axs[0].set_xlabel('observed value', fontsize = 45)
        axs[0].set_ylabel('frequency', fontsize = 45)


        axs[1].set_title('Gamma Results, n = '+ str(n_2), fontsize = 45)
        axs[1].set_xlabel('observed value', fontsize = 45)
        axs[1].set_ylabel('frequency', fontsize = 45)

        axs[2].set_title('Gamma Results, n = '+ str(n_3), fontsize = 45)
        axs[2].set_xlabel('observed value', fontsize = 45)
        axs[2].set_ylabel('frequency', fontsize = 45)
        
        plt.savefig("gamma.png")
        print([np.mean(u_n1.observations), np.std(u_n1.observations)])
        print([np.mean(u_n2.observations), np.std(u_n2.observations)])
        print([np.mean(u_n3.observations), np.std(u_n3.observations)])
        
class demo_geometric:
    
    def __init__(self,_n,_p):
        n_1 = _n
        n_2 = 2*n_1
        n_3 = 2*n_2

        u_n1   = rv.generate_geometric(n = n_1  , seed = 412, p = _p, unif_mult = 16807, unif_mod = (2**31)-1)
        u_n2  = rv.generate_geometric(n = n_2 , seed = 412  , p = _p, unif_mult = 16807, unif_mod = (2**31)-1)
        u_n3 = rv.generate_geometric(n = n_3, seed = 412    , p = _p, unif_mult = 16807, unif_mod = (2**31)-1)

        fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False,figsize=(55,20))

        axs[0].hist(u_n1.observations, bins=5)
        axs[1].hist(u_n2.observations, bins=10)
        axs[2].hist(u_n3.observations, bins=20)

        axs[0].set_title('Geometric Results, n = ' + str(n_1), fontsize = 45)
        axs[0].set_xlabel('observed value', fontsize = 45)
        axs[0].set_ylabel('frequency', fontsize = 45)


        axs[1].set_title('Geometric Results, n = '+ str(n_2), fontsize = 45)
        axs[1].set_xlabel('observed value', fontsize = 45)
        axs[1].set_ylabel('frequency', fontsize = 45)

        axs[2].set_title('Geometric Results, n = '+ str(n_3), fontsize = 45)
        axs[2].set_xlabel('observed value', fontsize = 45)
        axs[2].set_ylabel('frequency', fontsize = 45)
        
        plt.savefig("geometric.png")
        print([np.mean(u_n1.observations), np.std(u_n1.observations)])
        print([np.mean(u_n2.observations), np.std(u_n2.observations)])
        print([np.mean(u_n3.observations), np.std(u_n3.observations)])
        
class demo_normal:
    
    def __init__(self,_n,_mu,_sigma):
        n_1 = _n
        n_2 = 2*n_1
        n_3 = 2*n_2

        u_n1   = rv.generate_normal(n = n_1  , seed = 412, mu = _mu, sigma = _sigma, unif_mult = 16807, unif_mod = (2**31)-1)
        u_n2  = rv.generate_normal(n = n_2 , seed = 412, mu = _mu, sigma = _sigma, unif_mult = 16807, unif_mod = (2**31)-1)
        u_n3 = rv.generate_normal(n = n_3, seed = 412, mu = _mu, sigma = _sigma, unif_mult = 16807, unif_mod = (2**31)-1)

        fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False,figsize=(55,20))

        axs[0].hist(u_n1.observations, bins=5)
        axs[1].hist(u_n2.observations, bins=10)
        axs[2].hist(u_n3.observations, bins=20)

        axs[0].set_title('Normal Results, n = ' + str(n_1), fontsize = 45)
        axs[0].set_xlabel('observed value', fontsize = 45)
        axs[0].set_ylabel('frequency', fontsize = 45)


        axs[1].set_title('Normal Results, n = '+ str(n_2), fontsize = 45)
        axs[1].set_xlabel('observed value', fontsize = 45)
        axs[1].set_ylabel('frequency', fontsize = 45)

        axs[2].set_title('Normal Results, n = '+ str(n_3), fontsize = 45)
        axs[2].set_xlabel('observed value', fontsize = 45)
        axs[2].set_ylabel('frequency', fontsize = 45)
        
        plt.savefig("normal.png")
        print([np.mean(u_n1.observations), np.std(u_n1.observations)])
        print([np.mean(u_n2.observations), np.std(u_n2.observations)])
        print([np.mean(u_n3.observations), np.std(u_n3.observations)])        

        
class demo_triangular:
    
    def __init__(self,_n,_a,_c,_b):
        n_1 = _n
        n_2 = 2*n_1
        n_3 = 2*n_2

        u_n1 = rv.generate_triangular(n = n_1, seed = 412, a = _a, b = _b, c = _c, mult = 16807, mod = (2**31)-1)
        u_n2 = rv.generate_triangular(n = n_2, seed = 412  , a = _a, b = _b, c = _c, mult = 16807, mod = (2**31)-1)
        u_n3 = rv.generate_triangular(n = n_3, seed = 412    , a = _a, b = _b, c = _c, mult = 16807, mod = (2**31)-1)

        fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False,figsize=(55,20))

        axs[0].hist(u_n1.observations, bins=10)
        axs[1].hist(u_n2.observations, bins=20)
        axs[2].hist(u_n3.observations, bins=40)

        axs[0].set_title('Triangular Results, n = ' + str(n_1), fontsize = 45)
        axs[0].set_xlabel('observed value', fontsize = 45)
        axs[0].set_ylabel('frequency', fontsize = 45)


        axs[1].set_title('Triangular Results, n = '+ str(n_2), fontsize = 45)
        axs[1].set_xlabel('observed value', fontsize = 45)
        axs[1].set_ylabel('frequency', fontsize = 45)

        axs[2].set_title('Triangular Results, n = '+ str(n_3), fontsize = 45)
        axs[2].set_xlabel('observed value', fontsize = 45)
        axs[2].set_ylabel('frequency', fontsize = 45)
        
        plt.savefig("triangular.png")
        print([np.mean(u_n1.observations), np.std(u_n1.observations)])
        print([np.mean(u_n2.observations), np.std(u_n2.observations)])
        print([np.mean(u_n3.observations), np.std(u_n3.observations)])
        
class demo_uniform():
    
    def __init__(self,_n,_a,_b):
        n_1 = _n
        n_2 = 2*n_1
        n_3 = 2*n_2

        u_n1   = rv.generate_uniform(n = n_1  , seed = 412, a = _a, b = _b, mult = 16807, mod = (2**31)-1)
        u_n2  = rv.generate_uniform(n = n_2 , seed = 412, a = _a, b = _b, mult = 16807, mod = (2**31)-1)
        u_n3 = rv.generate_uniform(n = n_3, seed = 412, a = _a, b = _b, mult = 16807, mod = (2**31)-1)

        fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False,figsize=(55,20))

        axs[0].hist(u_n1.observations, bins=5)
        axs[1].hist(u_n2.observations, bins=10)
        axs[2].hist(u_n3.observations, bins=20)

        axs[0].set_title('Uniform Results, n = ' + str(n_1), fontsize = 45)
        axs[0].set_xlabel('observed value', fontsize = 45)
        axs[0].set_ylabel('frequency', fontsize = 45)


        axs[1].set_title('Uniform Results, n = '+ str(n_2), fontsize = 45)
        axs[1].set_xlabel('observed value', fontsize = 45)
        axs[1].set_ylabel('frequency', fontsize = 45)

        axs[2].set_title('Uniform Results, n = '+ str(n_3), fontsize = 45)
        axs[2].set_xlabel('observed value', fontsize = 45)
        axs[2].set_ylabel('frequency', fontsize = 45)
        
        plt.savefig("uniform.png")
        print([np.mean(u_n1.observations), np.std(u_n1.observations)])
        print([np.mean(u_n2.observations), np.std(u_n2.observations)])
        print([np.mean(u_n3.observations), np.std(u_n3.observations)])
        
class demo_weibull():
    
    def __init__(self,_n,_shape,_scale):
        n_1 = _n
        n_2 = 2*n_1
        n_3 = 2*n_2

        u_n1   = rv.generate_weibull(n = n_1  , seed = 412, _shape = _shape, _scale = _scale, mult = 16807, mod = (2**31)-1)
        u_n2  = rv.generate_weibull(n = n_2 , seed = 412, _shape = _shape, _scale = _scale, mult = 16807, mod = (2**31)-1)
        u_n3 = rv.generate_weibull(n = n_3, seed = 412, _shape = _shape, _scale = _scale, mult = 16807, mod = (2**31)-1)

        fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=False,figsize=(55,20))

        axs[0].hist(u_n1.observations, bins=5)
        axs[1].hist(u_n2.observations, bins=10)
        axs[2].hist(u_n3.observations, bins=20)

        axs[0].set_title('Weibull Results, n = ' + str(n_1), fontsize = 45)
        axs[0].set_xlabel('observed value', fontsize = 45)
        axs[0].set_ylabel('frequency', fontsize = 45)


        axs[1].set_title('Weibull Results, n = '+ str(n_2), fontsize = 45)
        axs[1].set_xlabel('observed value', fontsize = 45)
        axs[1].set_ylabel('frequency', fontsize = 45)

        axs[2].set_title('Weibull Results, n = '+ str(n_3), fontsize = 45)
        axs[2].set_xlabel('observed value', fontsize = 45)
        axs[2].set_ylabel('frequency', fontsize = 45)
        
        plt.savefig("weibull.png")
        print([np.mean(u_n1.observations), np.std(u_n1.observations)])
        print([np.mean(u_n2.observations), np.std(u_n2.observations)])
        print([np.mean(u_n3.observations), np.std(u_n3.observations)])
