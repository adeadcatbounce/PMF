# import libraries and packages

from scipy.stats import binom
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Scipy Binom - https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html
"""

# Estimating probability mass function to get k heads, in ten trials, with a probability of getting a heads (1/2)

number_heads = []
heads = []

for i in range(11):
    prob = binom.pmf(k=i, n=10, p=1/2)
    number_heads.append(i)
    heads.append(prob)

# Creating a dataframe to consolidate results

df = pd.DataFrame({'Column1' : number_heads, 'Column2': heads}).rename(columns={'Column1': 'Number of Heads', 'Column2' : 'P(Heads)'})
df['P(Heads)'] = df['P(Heads)'].round(decimals=2)

# Plot PMF
plt.title('Probability of Getting k (0 to 10) Heads in 10 Coin Flips \n Probability Mass Function (PMF) for a Fair Coin', fontsize=14)
plt.bar(x = 'Number of Heads', height='P(Heads)', width=5/10, color='firebrick', data=df)
plt.xlabel('Number of Heads in 10 Coin Flips', fontsize=12)
plt.ylabel('Probability of Getting this Many Heads', fontsize=12)
plt.yticks(np.arange(0,0.35, 0.05))
plt.xticks(np.arange(0,11,1))
plt.savefig('Output_Plot.png', dpi=1000)


