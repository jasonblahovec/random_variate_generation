# random_numbers
This module contains a series of Python classes that generate an array of observations for a given statistical distribution.  Each class in the module has a name of the form "generate*", where * can be any of:

  1.) uniform
  
  2.) normal
  
  3.) bernoulli
  
  4.) exponential
  
  5.) geometric
  
  ...
  

Each class accepts some input parameters to be described in detail below, and outputs self.observations, an array of length n (an input parameter) containing iid observations from the distribution specified by the class name.

Every class' input parameters follow a similar format:
--The first parameter is n, with a default value of 1000 for all distributions.
--The second parameter is the random seed to use.  The default value is 412, the country's premier area code.
-- Next are a series of distribution specific parameters:
    a. uniform: 2 parameters, a and b.  They default to a = 0 and b = 1, and are the upper and lower bound of the uniform distribution respectively.
    b. normal: 2 parameters, mu and sigma.  Need to update such that more than 0 and 1 are returned.
    c. bernoulli: 1 parameter, p.  p is the success probability for an individual trial.  the number of trials can be controlled with n.
    d. exponential: 1 parameter: lambda.
    e. geometric: 1 parameter: p, the success probability.  n is the first parameter
-- After the distribution specific stats are two parameters related to the uniforms generated underneath the distributions when applicable.  The last two parameters for each class are:
  a. unif_mult: the multiplier used in the Linear Congruential Generator used to produce uniforms.  defaults to 16807.
  b unif_mod: the modulus used in the LCG used in uniform calculation.  defaults to (2^31)-1.
  
  
