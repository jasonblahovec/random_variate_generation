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
    a. uniform
