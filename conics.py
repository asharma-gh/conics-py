import sys
import numpy as np
from matplotlib import pyplot as plt
#
XMIN,XMAX=-1000,1000
YMIN,YMAX=-1000,1000
STEP=8
EPSILON=.005
#
def parabola(x,a=1,h=0,k=0):
    return (((x-h)**2) / (4*a)) + k
#
def gen_points(fun,kwargs):
    domain=[n for n in range(XMIN,XMAX+1,STEP)]
    return domain,[parabola(x,**kwargs) for x in domain]
#
def _on_press(e):
    sys.stdout.flush()
    if e.key=='q':
        sys.exit(0)
#
def dist(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**.5
#
fig,axs=plt.subplots()
fig.canvas.mpl_connect('key_press_event',_on_press)
# Parabola
p={'a':100,'h':0,'k':0}
## Points
xs,ys=gen_points(parabola,p)
axs.plot(xs,ys,"bo",markersize=2)
## Foci
foc=(p['h'],p['k']+p['a'])
axs.plot(foc[0],foc[1],"ro")
## Directrix
dtx=p['k']-p['a']
axs.plot([XMIN,XMAX],[dtx]*2,"r")
### Prove condition [forall p, dist(p,foci)=dist(p,directrix)
cond=True
for ii,xx in enumerate(xs):
    if not(abs(dist((xx,ys[ii]),foc)-dist((xx,ys[ii]),(xx,dtx))) < EPSILON):
        cond=False
        print(xx,ys[ii],foc,dtx,dist((xx,ys[ii]),foc),dist((xx,ys[ii]),(xx,dtx)))
if cond:
    print("[Parabola] - Condition Holds")
# Axis
axs.plot([XMIN,XMAX],[0,0],"k")
axs.plot([0,0],[min(ys),max(ys)],"k")
plt.show()

