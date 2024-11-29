import matplotlib.pyplot as plt
import matplotlib
import csv
import pandas as pd


matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})


df1 = pd.read_csv('65pH/Set1.csv')
data1 = pd.DataFrame(df1, columns=['Wavelength', ' Absorbance'])
ax2 = data1.plot(x = 'Wavelength', y = ' Absorbance',  label='S1')
yabs_max = abs(max(ax2.get_ylim(), key=abs))
xabs_max = abs(max(ax2.get_xlim(), key=abs))
ax2.set_ylim(ymin=-0.02, ymax=0.15)
ax2.set_xlim(xmin=380.5, xmax=xabs_max)
ax2.set_xlabel("Wavelength")
ax2.set_ylabel("Absorbance")

df2 = pd.read_csv('65pH/Set2.csv')
data2 = pd.DataFrame(df2, columns=['Wavelength', ' Absorbance'])
ax4 = data2.plot(x = 'Wavelength', y = ' Absorbance', ax=ax2,  label='S2')

df3 = pd.read_csv('65pH/Set3.csv')
data3 = pd.DataFrame(df3, columns=['Wavelength', ' Absorbance'])
ax5 = data3.plot(x = 'Wavelength', y = ' Absorbance', ax=ax2,  label='S3')

plt.title("Spectrophotometry of 6.5 pH phytoplankton")

plt.savefig('sixfiveph.pgf')
plt.show()