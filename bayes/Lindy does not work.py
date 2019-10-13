#!/usr/bin/env python
# coding: utf-8

# https://medium.com/@QwQiao/statistical-fallacy-behind-the-lindy-effect-b115049dbbab

# In[4]:


import random
import numpy as np
import matplotlib.pyplot as plt

sample = 10000


# In[5]:


# Take a random sample of total lifespans
# Use exponential distribution

total_life = np.random.exponential(scale=1.0, size=sample)


# In[6]:


# For each data point, initial current age
# Current age follows uniform distribution between 0 and total lifespan
# Also initial future life expectancy

age = []
future_life_expectancy = []

for l in total_life:
    random_age = np.random.uniform(0, 1)
    age.append(random_age)
    
    random_future_life_expectancy = l - random_age
    future_life_expectancy.append(random_future_life_expectancy)


# In[7]:


# Compute line of best fit

Y = future_life_expectancy
X = age

from scipy.odr import Model, Data, ODR
from scipy.stats import linregress

def f(p, x):
    return (p[0] * x) + p[1]

linreg = linregress(X, Y)
mod = Model(f)
dat = Data(X, Y)
od = ODR(dat, mod, beta0=[1., 2.])
out = od.run()
TLSbeta = out.beta[0]


# In[15]:


# Plot chart

plt.plot(X, Y, '.')
plt.plot(X, out.beta[1] + np.multiply(X, out.beta[0]), '.')

plt.xlabel('Current Age')
plt.ylabel('Future Life')
plt.title('Future Life Expectancy')
plt.show()
#plt.savefig('Lindy not true')
#plt.clf()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




