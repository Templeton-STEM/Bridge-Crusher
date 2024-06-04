import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
import numpy as np
header = ['Port 0', 'Port 1', 'Port 2', 'Port 3']
fig, axd = plt.subplot_mosaic([['tl', 'tr'],['b', 'b']], constrained_layout = True)
plt.style.use('Solarize_Light2')
ax1 = axd['b']
ax2 = axd['tl']
ax3 = axd['tr']
sumar = []
tar= []
max = [0]
COLOR = 'red'
mpl.rcParams['text.color'] = COLOR
mpl.rcParams['axes.labelcolor'] = COLOR
mpl.rcParams['xtick.color'] = COLOR
mpl.rcParams['ytick.color'] = COLOR
def animate(i):
    pullData = open("data.txt","r+").readline()
    sum = np.array([0, 255])
    dataArray = pullData.split(' ')
    ax2.clear()
    ax1.clear()
    ax3.clear()
    ax3.set_yticks([])
    ax3.set_xticks([])
    dataArray[0] = round((float(dataArray[0])) / 240) + 6
    dataArray[1] = round((float(dataArray[1])) / 240) + 1
    dataArray[2] = round((float(dataArray[2])) / 240) - 1
    dataArray[3] = round((float(dataArray[3])) / 240) + 5
    sum[0] = dataArray[0] +  dataArray[1] +  dataArray[2] + dataArray[3]
    sum[1] = 0
    if sum[0] > max[0]:
        max[0] = sum[0]
    sumar.append(sum[0])
    tar.append(i * 0.5)
    st = ax3.text(0.65, 0.25, str(sum[0]), ha = 'center', va = 'center', size = 25, color = 'black')
    st = ax3.text(0.5, 0.25,'force on the bridge: ' + '        ' +  ' lbs', ha = 'center', va = 'center', size = 16)
    st = ax3.text(0.6, 0.75, str(max[0]).upper() , ha = 'center', va = 'center', size = 25, color = 'black')
    st = ax3.text(0.5, 0.75,'largest force:           lbs', ha = 'center', va = 'center', size = 16)
    ax2.set(ylim=(0, 200), yticks= np.arange(0, 200, 20))
    try:
        normal = ((sum[0] - 0) / (400 - 0))
    except RuntimeWarning:
        pass
    print(normal)
    try:
        ax2.bar(header, dataArray, color = (normal, 0, 1 - normal, 1))
    except ValueError:
        ax2.bar(header, dataArray, color = 'red')
    ax2.set_ylabel('lbs')
    ax1.plot(tar, sumar, color='blue')
    ax1.set_xlabel('seconds')
    ax1.set_ylabel('lbs')

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
