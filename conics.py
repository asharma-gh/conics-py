import sys
import numpy as np
from matplotlib import pyplot as plt
#
XMIN,XMAX=-1000,1000
YMIN,YMAX=-1000,1000
STEP=.05
EPSILON=.005
INVALID_NUM="NAN"
#
def parabola(x,a=1,h=0,k=0):
    return (((x-h)**2) / (4*a)) + k
#
def ellipse(x,a=1,b=1,h=0,k=0):
    # Only valid for |x| <= a+h
    if abs(x)>(a+h):
        return INVALID_NUM
    radc=b*((((-1*((x-h)**2))/(a**2))+1)**.5)
    return k+radc,k-radc
#
def gen_points(fun,kwargs):
    domain=[n for n in np.arange(XMIN,XMAX+1,STEP)]
    xs=[]
    ys=[]
    for d in domain:
        res=fun(d,**kwargs)
        if res != INVALID_NUM:
            xs.append(d)
            ys.append(res)
    return xs,ys
#
def _on_press(e):
    sys.stdout.flush()
    if e.key=='q':
        sys.exit(0)
#
def dist(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**.5
#
def draw_p(axs):
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
    return xs,ys
# 
def draw_e(axs):
    p={'a':10,'h':0,'k':50,'b':5}
    xs,ys=gen_points(ellipse,p)
    yn=[]
    for ii,x in enumerate(xs):
        axs.plot(x,ys[ii][0],"bo",markersize=2)
        axs.plot(x,ys[ii][1],"bo",markersize=2)
        yn.append(ys[ii][0])
        yn.append(ys[ii][1])
    ## Foci 
    c=((p['a']**2)-(p['b']**2))**.5
    foc=((p['h']-c,p['k']),(p['h']+c,p['k']))
    axs.plot(foc[0][0],foc[0][1],"ro")
    axs.plot(foc[1][0],foc[1][1],"ro")
    ## Center axis
    axs.plot(p['h'],p['k'],"bo")
    axs.plot([min(xs),max(xs)],[p['k']]*2,"k")
    axs.plot([p['h']]*2,[min(yn),max(yn)],"k")
    return xs,ys
#
fig,axs=plt.subplots()
axs.set_aspect('equal')
fig.canvas.mpl_connect('key_press_event',_on_press)
# Parabola
##_,ys=draw_p(axs)
# Eliipse
_,ys=draw_e(axs)
plt.show()

