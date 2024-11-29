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


df1 = pd.read_csv('Control/Set2.csv')
data1 = pd.DataFrame(df1, columns=['Wavelength', ' Absorbance'])
ax2 = data1.plot(x = 'Wavelength', y = ' Absorbance',  label='C1')
yabs_max = abs(max(ax2.get_ylim(), key=abs))
xabs_max = abs(max(ax2.get_xlim(), key=abs))
ax2.set_ylim(ymin=-0.02, ymax=0.08)
ax2.set_xlim(xmin=380.5, xmax=xabs_max)
ax2.set_xlabel("Wavelength")
ax2.set_ylabel("Absorbance")

df2 = pd.read_csv('Control/Set3.csv')
data2 = pd.DataFrame(df2, columns=['Wavelength', ' Absorbance'])
ax4 = data2.plot(x = 'Wavelength', y = ' Absorbance', ax=ax2,  label='C2')

df3 = pd.read_csv('Control/Set4.csv')
data3 = pd.DataFrame(df3, columns=['Wavelength', ' Absorbance'])
ax5 = data3.plot(x = 'Wavelength', y = ' Absorbance', ax=ax2,  label='C3')


df4 = pd.read_csv('Control/Set5.csv')
data4 = pd.DataFrame(df4, columns=['Wavelength', ' Absorbance'])
ax7 = data4.plot(x = 'Wavelength', y = ' Absorbance', ax=ax2,  label='C4')


df5 = pd.read_csv('Control/Set6.csv')
data5 = pd.DataFrame(df5, columns=['Wavelength', ' Absorbance'])
ax9 = data5.plot(x = 'Wavelength', y = ' Absorbance', ax=ax2,  label='C5')


df6 = pd.read_csv('Control/Set7.csv')
data6 = pd.DataFrame(df6, columns=['Wavelength', ' Absorbance'])
ax11 = data6.plot(x = 'Wavelength', y = ' Absorbance', ax=ax2, label='C6')

plt.title("Spectrophotometry of Control Solutions (no modifications)")

plt.savefig('controls.pgf')
plt.show()