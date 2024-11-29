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

df1 = pd.read_csv('Acids/Set1.csv')
data1 = pd.DataFrame(df1, columns=['Wavelength', ' Absorbance'])
ax2 = data1.plot(x = 'Wavelength', y = ' Absorbance',  label='6 pH')
yabs_max = abs(max(ax2.get_ylim(), key=abs))
xabs_max = abs(max(ax2.get_xlim(), key=abs))
ax2.set_ylim(ymin=-0.03, ymax=0.07)
ax2.set_xlim(xmin=380.5, xmax=xabs_max)
ax2.set_xlabel("Wavelength")
ax2.set_ylabel("Absorbance")

df2 = pd.read_csv('Acids/Set2.csv')
data2 = pd.DataFrame(df2, columns=['Wavelength', ' Absorbance'])
ax4 = data2.plot(x = 'Wavelength', y = ' Absorbance', ax=ax2,  label='5.5 pH')

df3 = pd.read_csv('Acids/Set3.csv')
data3 = pd.DataFrame(df3, columns=['Wavelength', ' Absorbance'])
ax5 = data3.plot(x = 'Wavelength', y = ' Absorbance', ax=ax2,  label='6.5 pH')


df4 = pd.read_csv('Acids/Set4.csv')
data4 = pd.DataFrame(df4, columns=['Wavelength', ' Absorbance'])
ax7 = data4.plot(x = 'Wavelength', y = ' Absorbance', ax=ax2,  label='7.5 pH')


df5 = pd.read_csv('Acids/Set5.csv')
data5 = pd.DataFrame(df5, columns=['Wavelength', ' Absorbance'])
ax9 = data5.plot(x = 'Wavelength', y = ' Absorbance', ax=ax2,  label='8 pH')


df6 = pd.read_csv('Acids/Set6.csv')
data6 = pd.DataFrame(df6, columns=['Wavelength', ' Absorbance'])
ax11 = data6.plot(x = 'Wavelength', y = ' Absorbance', ax=ax2, label='5 pH')

df7 = pd.read_csv('Acids/Set7.csv')
data7 = pd.DataFrame(df7, columns=['Wavelength', ' Absorbance'])
ax13 = data7.plot(x = 'Wavelength', y = ' Absorbance', ax=ax2, label='7 pH')

plt.title("Spectrophotometry of Acid and Base Control Solutions")

plt.savefig('main.pgf')
plt.show()
