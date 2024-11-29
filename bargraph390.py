import matplotlib.pyplot as plt
import matplotlib
import csv
import pandas as pd
import seaborn as sns

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

df = pd.read_csv('SRPPeaks/390srp.csv')
print(df)
data = pd.DataFrame(df, columns=['pH', 'TRIAL 1','TRIAL 2','TRIAL 3'])

df.plot(x='pH', 
        kind='bar', 
        stacked=False, 
        title='390nm peaks of phytoplankton chlorophyll') 

plt.savefig('bar390.pgf')
plt.show()
