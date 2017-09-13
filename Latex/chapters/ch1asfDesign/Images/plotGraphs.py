import numpy as np
import matplotlib.pyplot as plt
import matplotlib

print matplotlib.style.available

matplotlib.style.use("seaborn-whitegrid")
matplotlib.rc('ytick', labelsize=16) 
matplotlib.rc('xtick', labelsize=16) 
matplotlib.rcParams.update({'font.size': 18})

#Module Distance Graph

def adjustFigAspect(fig,aspect=1):
    '''
    Adjust the subplot parameters so that the figure has the correct
    aspect ratio.
    '''
    xsize,ysize = fig.get_size_inches()
    minsize = min(xsize,ysize)
    xlim = .4*minsize/xsize
    ylim = .4*minsize/ysize
    if aspect < 1:
        xlim *= aspect
    else:
        ylim /= aspect
    fig.subplots_adjust(left=.5-xlim,
                        right=.5+xlim,
                        bottom=.5-ylim,
                        top=.5+ylim)


module_distance = np.arange(0,110,10)
pv_electricity = np.array([51,53,52.5,51,49,45,43,40,35.5,35,32.5])

frame_size = np.arange(0,9)
frame_size_util = np.array([144.4,131.1,109.9,103.6,95.1,90.4,82.9,78.7,69.8])

struc_depth = np.array([0.12,0.15,0.18,0.2,0.23,0.25,0.3,0.4,0.45,0.5])
struc_depth_util = np.array([134.6,94.8,81.8,76.7,70,65.6,56.6,42.8,41.5,41.5])


fig = plt.figure()
plt.plot(module_distance,pv_electricity, 'k', marker='o',markersize=10,markeredgewidth=1,linestyle='-', markerfacecolor="None")
plt.xlabel('Module Distance %')
plt.ylabel('PV electricity (kWh/year/m2)')
adjustFigAspect(fig,aspect=1.8)
plt.show()
fig.savefig('modulespacing2.pdf', format='pdf', bbox_inches='tight')

matplotlib.rc('xtick', labelsize=10) 
fig = plt.figure()
plt.plot(frame_size,frame_size_util, 'k', marker='o',markersize=10,markeredgewidth=1,linestyle='-', markerfacecolor="None")
plt.xlabel('Frame Size [H x W x 0.5cm] (cm)')
plt.ylabel('Max Abs. Utilisation \n (% of yield strength)')

plt.xticks([0,1,2,3,4,5,6,7,8], ['12x12', '13x13', '15x15', '16x15', '18x15', '20x15', '25x15', '30x15', 'Point \n Mountings'])
adjustFigAspect(fig,aspect=1.8)
plt.show()
fig.savefig('ASF_FrameSize.pdf', format='pdf', bbox_inches='tight')

matplotlib.rc('xtick', labelsize=16) 
fig = plt.figure()
plt.plot(struc_depth,struc_depth_util, 'k', marker='o',markersize=10,markeredgewidth=1,linestyle='-', markerfacecolor="None")
plt.xlabel('Structural Depth (m)')
plt.ylabel('Max Abs. Utilisation \n (% of yield strength)')
adjustFigAspect(fig,aspect=1.8)
plt.show()
fig.savefig('ASF_Structure.pdf', format='pdf', bbox_inches='tight')


