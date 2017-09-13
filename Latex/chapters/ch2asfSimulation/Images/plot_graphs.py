import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import sys


#print sys.executable
matplotlib.rc('ytick', labelsize=16) 

plt.style.use('seaborn-white')


fig=plt.Figure()
fig.set_canvas(plt.gcf().canvas)


df=pd.read_csv('yearlyDataCOP1_3.csv')
dfPV=df[df.Zuerich_Kloten_2005 == 'PV']
df = df[df.Zuerich_Kloten_2005 != 'E_HCL']
df = df[df.Zuerich_Kloten_2005 != 'E']
df = df[df.Zuerich_Kloten_2005 != 'PV']


data2=df.values.T.tolist()

data = [data2[1],data2[2],data2[3]]
y_max= sum(max(data)) + 500
data=zip(*data)

PV_data=dfPV.values.T.tolist()
PV_data= PV_data[1:4]
PV_data = [val for sublist in PV_data for val in sublist]
print PV_data


columns = ('No Shading', 'Static Panels', 'ASF')
rows = ['%d year' % x for x in (100, 50, 20)]

values = np.arange(0, 2500, 500)
value_increment = 1000

# Get some pastel shades for the colors
colors = plt.cm.PuBu(np.linspace(0.3, 0.8, len(rows)+1))

n_rows = len(data)


bar_width = 0.4
index = np.arange(len(columns)) + 0.3
index2 = np.arange(len(columns)) + 0.3+bar_width


# Initialize the vertical-offset for the stacked bar chart.
y_offset = np.array([0.0] * len(columns))
print y_offset

# Plot bars and create text labels for the table
cell_text = []
build=[]
for row in range(n_rows):
    build.append(plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row], edgecolor="None"))
    PV=plt.bar(index2, PV_data, bar_width, color=colors[3], edgecolor="None")
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x/1000.0) for x in y_offset])
# Reverse colors and text labels to display the last value at the top.
colors = colors[::-1]
cell_text.reverse()

# # Add a table at the bottom of the axes
# the_table = plt.table(cellText=cell_text,
#                       rowLabels=rows,
#                       rowColours=colors,
#                       colLabels=columns,
#                       loc='bottom')

# Adjust layout to make room for the table:
plt.subplots_adjust(left=0.2, bottom=0.2)

plt.ylabel("Electricity Load/Generation (kWh/year)", fontsize=18)

plt.xticks(index2, columns, fontsize=18)
plt.legend([build[2],build[1],build[0],PV],['Lighting','Heating','Cooling','PV'], fontsize=18)


plt.ylim(0,y_max)
#plt.title('Energy Consumption')

plt.show()

fig.savefig('compare_facadesCOP1_3.pdf', format='pdf', bbox_inches='tight')


