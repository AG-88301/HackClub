import matplotlib.pyplot as plt
import numpy as np
from math import log, sqrt

def dtModel(theta, u, dt=0.02, g=9.81, h=0):
    vx = u*np.cos(theta)
    vy = u*np.sin(theta)

    x, y = [0], [h]
    while y[-1] >= 0:   
        x.append(x[-1] + vx*dt)
        y.append(y[-1] + vy*dt)
        vy -= g*dt
        
    return x, y

def maxRange(theta, u, g=9.81, h=0):
    return (u**2)/g * (np.sin(theta) * np.cos(theta) + np.cos(theta) * np.sqrt(np.sin(theta)**2 + 2*g*h/u**2)) #range

def analyticModel(theta, u, g=9.81, h=0, **_):
    r = maxRange(theta=theta, u=u, g=g, h=h)
    x = np.linspace(0,r,1000)
    y = h + x*np.tan(theta) - g/(2*u**2)*(1+np.tan(theta)**2)*x**2
    
    return x, y, r

def apogee(theta, u, g=9.81, h=0):
    xa = u**2/g * np.sin(theta) * np.cos(theta)
    ya = h + u**2/(2*g) * np.sin(theta)**2

    return xa, ya

def analyticModelToTarget_x(target_x, theta, u, g=9.81, h=0):
    x = np.linspace(0,target_x,1000)
    y = h + x*np.tan(theta) - g/(2*u**2)*(1+np.tan(theta)**2)*x**2
    
    return x, y
    
def getMinUAndTheta(x, y, g=9.81, h=0):
    y -= h
    min_u = np.sqrt(g * (y + np.sqrt(x**2+y**2)))
    theta = np.arctan2(y + np.sqrt(x**2+y**2),x)
    
    return min_u, theta
    
def getHighAndLowTheta(u, x, y, g=9.81, h=0):
    a = (x**2 * g) / (2 * u**2)
    b = -x
    c = y - h + ((g * x**2) / (2*u**2))

    highTheta = np.arctan2(-b + np.sqrt(b**2 - 4*a*c),2*a)
    lowTheta = np.arctan2(-b - np.sqrt(b**2 - 4*a*c),2*a)
    
    return highTheta, lowTheta

def dtBounce(c, h, theta, u, dt=0.01, numOfBounces=5, g=9.81):
    bounces = 0
    x, y = [0], [h]
    vx, vy = u*np.cos(theta), u*np.sin(theta)
    
    while bounces < numOfBounces:
        x.append(x[-1] + vx*dt)
        y.append(y[-1] + vy*dt - 0.5 * g * dt**2)
        vy -= g * dt
        if y[-1] < 0:#if bounce
            y[-1] = 0
            vy = -c * vy
            bounces += 1
            
    return x, y

def thetaMax(u, g=9.81, h=0):
    return np.arcsin(1/np.sqrt(2+2*g*h/u**2))
    
def zfunc(z):
    return 0.5*log(abs(sqrt(1+z**2) + z)) + 0.5*z*sqrt(1 + z**2)

def calcLength(theta, u, g=9.81, h=0):
    r = maxRange(theta=theta, u=u, g=g, h=h)
    a = (u**2)/(g * (1 + (np.tan(theta))**2))
    b = np.tan(theta)
    c = np.tan(theta) - g*r*( 1 + (np.tan(theta))**2 )/(u**2)
    s = a * (zfunc(b) - zfunc(c))
    return s

def boundingParabola(u, g=9.81, h=0):
    r = maxRange(theta=thetaMax(u=u, g=g, h=h), u=u, g=g, h=h)
    x = np.linspace(0,r,1000)
    y = h + u**2/2/g -g* x**2 / 2 / u**2
    return x, y