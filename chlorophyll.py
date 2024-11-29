import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import seaborn as sns

df660 = pd.read_csv('SRPPeaks/avgs.csv')
data660 = pd.DataFrame(df660, columns=['pH','660 nm'])
chloro = [0,0,0,0,0,0,0]

matplotlib.use("pgf")
matplotlib.rcParams.update({
   "pgf.texsystem": "pdflatex",
  'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

for x in range(7):
    chloro[x] = ((data660.at[x, "660 nm"]).item()/(4.4 * pow(10, (-4))))

plots = pd.DataFrame(chloro, index=data660.get('pH'))
ax = plots.plot(
        kind='bar', 
        stacked=False, 
        ylabel='mol/liter',
        title='Chlorophyll Levels at Each pH')
plt.savefig('chloro.pgf')
plt.show()
