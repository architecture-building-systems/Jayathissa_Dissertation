import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


plt.style.use('ggplot')


df=pd.read_csv('transientAngles.csv', index_col=0, header=None)
MappedData=map(list,df.values)



X_Angles1=MappedData[0]
Y_Angles1=MappedData[1]
temp1=MappedData[2]
X_Angles2=MappedData[3]
Y_Angles2=MappedData[4]
temp2=MappedData[5]
X_Angles3=MappedData[6]
Y_Angles3=MappedData[7]
temp3=MappedData[8]
print temp1


# X_Angles1=[0,45,45,45,30,30,30,45,90,45,45,45]
# Y_Angles1=[15,15,30,30,15,15,-15,-15,-15,-15,0,0]
# temp1=[19,19,20,21,22,23,24,22,23,20,19,18]

# X_Angles2=[0,45,45,45,30,30,30,45,90,45,45,45]
# Y_Angles2=[15,15,30,30,15,15,-15,-15,-15,-15,0,0]
# temp2=[19,19,20,21,22,23,24,22,23,20,19,18]

# X_Angles3=[0,45,45,45,30,30,30,45,90,45,45,45]
# Y_Angles3=[15,15,30,30,15,15,-15,-15,-15,-15,0,0]
# temp3=[19,19,20,21,22,23,24,22,23,20,19,18]


hours=range(8,20,1)



# print hours
# print len(X_Angles1)
# print len(Y_Angles1)
# print len(hours)
# print len(temp1)

fig=plt.Figure()
fig.set_canvas(plt.gcf().canvas)



ax1=plt.subplot(311)
lns1=ax1.plot(hours,X_Angles1, label='Azimuth Angles')
lns2=ax1.plot(hours,Y_Angles1, label='Altitude Angles')
ax1.set_title('Sunny day')
ax1.set_ylabel('Angle (deg)')
ax1.set_xlabel('Hour of the Day')


ax2=ax1.twinx()
lns3=ax2.plot(hours,temp1, color=plt.rcParams['axes.color_cycle'][3],label='Indoor Temperature')
ax2.set_ylabel('Temperature (C)')



ax3=plt.subplot(312)
ax3.plot(hours,X_Angles2,hours,Y_Angles2)
ax3.set_title('Cloudy day')
ax3.set_ylabel('Angle (deg)')
ax3.set_xlabel('Hour of the Day')

ax4=ax3.twinx()
ax4.plot(hours,temp2, color=plt.rcParams['axes.color_cycle'][3])
ax4.set_ylabel('Temperature (C)')

ax5=plt.subplot(313)
ax5.plot(hours,X_Angles3,hours,Y_Angles3)
ax5.set_title('Sunny day with clouds in the afternoon')
ax5.set_ylabel('Angle (deg)')
ax5.set_xlabel('Hour of the Day')

ax6=ax5.twinx()
ax6.plot(hours,temp3, color=plt.rcParams['axes.color_cycle'][3])
ax6.set_ylabel('Temperature (C)')

lns = lns1+lns2+lns3
labs = [l.get_label() for l in lns]

lgd=ax1.legend(lns, labs, loc=4,bbox_to_anchor=(0.9,-4.5), ncol=3)
#lgd=ax1.legend(lns, labs, loc=1, bbox_to_anchor=(1.4,1))
#ax1.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,borderaxespad=0.,ncol=2, mode="expand",)





plt.tight_layout()

#plt.show()

# Adjust layout to make room for the table:
# plt.subplots_adjust(left=0.2, bottom=0.2)

# plt.ylabel("Energy Load/Generation (kWh/year)")
# plt.xticks(index2, columns)



# plt.ylim(0,y_max)
#plt.title('Energy Comsumption')
fig.savefig('transientPlot.pdf', format='pdf', bbox_extra_artists=(lgd,), bbox_inches='tight')