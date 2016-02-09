import stepAnimation
from math import *

xdistance=160                     #distances  on x axis between center points
ydistance=120                     #distances on y axis between center points
colormax=255 
row=5
column=5  
def rgbString(red, green, blue):  #helper function
    return "#%02x%02x%02x" % (red, green, blue)
def colorR(y):                    # get the value of R
    red=(y/ydistance)*(colormax/column-1)
    return red
def colorG(x):                    # get the value of G
    green=(colormax/(row-1))*((row-1)-x/xdistance)
    return green
colorB=0                          # the value of B
def fancyWheelGridAnimation(canvas,width,height,step):
    x1=80                
    y1=60                         # first polygon's center point       
    
    m=(2*pi)*(10.0/360)           # rotate of each step
    r=55                          #radius of each polygon

    for x in xrange(x1,x1+column*xdistance,xdistance) :  
        for y in xrange(y1,y1+row*ydistance,ydistance): 
            h=(x/xdistance)+(y/ydistance)+4         
            for a in xrange(0,h):                   
                for b in xrange(0,h):             
                    if h%2==0:                     
            
                        canvas.create_line(x+r*cos((a*2*pi/h)-(step*m)),
                            y-r*sin((a*2*pi/h)-(step*m)),
                            x+r*cos((b*2*pi/h)-(step*m)),
                            y-r*sin((b*2*pi/h)-(step*m)),
                            fill=rgbString(colorR(y),colorG(x),colorB))
                    else:                         
                        canvas.create_line(x+r*cos((a*2*pi/h)+(step*m)),
                            y-r*sin((a*2*pi/h)+(step*m)),
                            x+r*cos((b*2*pi/h)+(step*m)),
                            y-r*sin((b*2*pi/h)+(step*m)),
                            fill=rgbString(colorR(y),colorG(x),colorB))
                        
stepAnimation.run(fancyWheelGridAnimation,width=800,height=600,timerDelay=128)

