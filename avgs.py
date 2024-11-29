import matplotlib.pyplot as plt
import matplotlib
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
df660 = pd.read_csv('SRPPeaks/660srp.csv')

data = pd.DataFrame(df, columns=['pH', 'TRIAL 1','TRIAL 2','TRIAL 3'])
data660 = pd.DataFrame(df660, columns=['pH', 'TRIAL 1','TRIAL 2','TRIAL 3'])
avg3 = [0, 0, 0, 0, 0, 0, 0]
avg6 = [0, 0, 0, 0, 0, 0, 0]

for x in range(7):
    avg3[x] = (((data.at[x, "TRIAL 1"] + data.at[x, "TRIAL 2"] + data.at[x, "TRIAL 3"]).item())/3)
    avg6[x] = (((data660.at[x, "TRIAL 1"] + data660.at[x, "TRIAL 2"] + data660.at[x, "TRIAL 3"]).item())/3)

df666 = pd.DataFrame(data={"pH": data.get('pH'), "660 nm": avg6})
df666.to_csv("./avgs.csv", sep=',',index=False)


y_errormin3 = [0, 0, 0, 0, 0, 0, 0]
y_errormax3 = [0, 0, 0, 0, 0, 0, 0]
y_errormin6 = [0, 0, 0, 0, 0, 0, 0]
y_errormax6 = [0, 0, 0, 0, 0, 0, 0]


for x in range(7):
    y_errormin3[x] = avg3[x] - min(min(data.at[x, "TRIAL 1"], data.at[x, "TRIAL 2"]), data.at[x, "TRIAL 3"]).item()
    y_errormax3[x] = max(max(data.at[x, "TRIAL 1"], data.at[x, "TRIAL 2"]), data.at[x, "TRIAL 3"]).item() - avg3[x]
    y_errormin6[x] = avg6[x] - min(min(data660.at[x, "TRIAL 1"], data660.at[x, "TRIAL 2"]), data660.at[x, "TRIAL 3"]).item()
    y_errormax6[x] = max(max(data660.at[x, "TRIAL 1"], data660.at[x, "TRIAL 2"]), data660.at[x, "TRIAL 3"]).item() - avg6[x]

error390 = {avg3[0]: {'min': y_errormin3[0],'max': y_errormax3[0]}, avg3[1]: {'min': y_errormin3[1],'max': y_errormax3[1]}, avg3[2]: {'min': y_errormin3[2],'max': y_errormax3[2]}, avg3[3]: {'min': y_errormin3[3],'max': y_errormax3[3]}, avg3[4]: {'min': y_errormin3[4],'max': y_errormax3[4]}, avg3[5]: {'min': y_errormin3[5],'max': y_errormax3[5]}, avg3[6]: {'min': y_errormin3[6],'max': y_errormax3[6]}}
error660 = {avg6[0]: {'min': y_errormin6[0],'max': y_errormax6[0]}, avg6[1]: {'min': y_errormin6[1],'max': y_errormax6[1]}, avg6[2]: {'min': y_errormin6[2],'max': y_errormax6[2]}, avg6[3]: {'min': y_errormin6[3],'max': y_errormax6[3]}, avg6[4]: {'min': y_errormin6[4],'max': y_errormax6[4]}, avg6[5]: {'min': y_errormin6[5],'max': y_errormax6[5]}, avg6[6]: {'min': y_errormin6[6],'max': y_errormax6[6]}}

z = {**error390, **error660}
df6 = pd.DataFrame(data={"pH": data.get("pH"),"390 nm": avg3, "660 nm": avg6})
ax = df6.plot(x='pH', 
        kind='bar', 
        stacked=False, 
        title='Average absorbance at both 390nm and 660nm')
plt.xlabel('pH')
plt.ylabel('Absorbance')

for p in ax.patches:
    x = p.get_x()  # get the bottom left x corner of the bar
    w = p.get_width()  # get width of bar
    h = p.get_height()  # get height of bar
    min_y = z[h]['min']  # use h to get min from dict z
    max_y = z[h]['max']  # use h to get max from dict z
    plt.vlines(x+w/2, min_y, max_y, color='k')  # draw a vertical line

plt.savefig('avgs.pgf')
plt.show()
