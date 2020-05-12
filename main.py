import numpy as np
import sys
from os import system, remove, chdir
import time
start = time.time()
height = 1  #   meters
width = 1   #   meters
dx = 0.01
dy = 0.01
nt = 4000
time_step = 400
T_initial = 300
T_left = 1200
T_right = 300
T_top = 300
T_bottom = 300
#height = float(input())
#width = float(input())
#dx = float(input())
#dy = float(input())
#nt = int(input())
#time_step = int(input())
#T_initial = float(input())
#T_left = float(input())
#T_right = float(input())
#T_bottom = float(input())
#T_top = float(input())
nx = int(round(width/dx)) + 1
ny = int(round(height/dy)) + 1

x = np.zeros((nx*ny))
y = np.zeros((nx*ny))
data = np.zeros((nx*ny,3))
T = np.zeros((nx,ny))
T += T_initial    #   Initialization
T[0,:] = T_left       #       Left Boundary
T[nx-1,:] = T_right       #       Right Boundary
T[:,0] = T_bottom       #       Bottom Boundary
T[:,ny-1] = T_top       #       Top Boundary
T_new = T*1.0
cbmin = T.min()
cbmax = T.max()
#   Properties
#k = 
#rho = 
#cp = 
#alpha = k/(rho*cp)
alpha = 0.001
courant_num = 0.5
dt = (courant_num*dx**2)/(2*alpha)
cx = courant_num*0.5
cy = courant_num*0.5
ver = 1
###############################################
print("Height = ",height,"\n")
print("Width = ",width,"\n")
print("Grid size along width = ",dx,"\n")
print("Grid size along heigth = ",dy,"\n")
print("Number of time steps = ",nt,"\n")
print("Time step interval to save data = ",time_step,"\n")
print("Initial Temperature = ",T_initial,"K\n")
print("Left Boundary Temperature = ",T_left,"K\n")
print("Right Boundary Temperature = ",T_right,"K\n")
print("Bottom Boundary Temperature = ",T_bottom,"K\n")
print("Top Boundary Temperature = ",T_top,"K\n")
###############################################
chdir("./data")
###############################################
for j in range (0,ny):
    for i in range (0,nx):
        x[i+j*nx] = i*dx
        data[i+j*nx,2] = T_new[i,j]*1.0
for j in range (0,ny):
    for i in range (0,nx):
        y[i+j*nx] = j*dy
data[:,0] = x*1.0
data[:,1] = y*1.0
ti = 0
np.savetxt('time_step_'+str(ti)+'.dat',data)
system('gnuplot -e "filename=\'%s\';cbmin=\'%f\';cbmax=\'%f\'" contour.gp'%(ti,cbmin,cbmax))
for t in range (0,nt):
    for j in range (1,ny-1):
        for i in range (1,nx-1):
            T_new[i,j] = T[i,j] + cx*(T[i,j+1]-2*T[i,j]+T[i,j-1]) + cy*(T[i+1,j]-2*T[i,j]+T[i-1,j])
            data[i+j*nx,2] = T_new[i,j]*1.0
    T = T_new*1.0
    if t==time_step*ver-1:
        ver+=1
        #ti = round((t+1)*dt,4)
        ti = t+1
        np.savetxt('time_step_'+str(ti)+'.dat',data)
        system('gnuplot -e "filename=\'%s\';cbmin=\'%f\';cbmax=\'%f\'" contour.gp'%(ti,cbmin,cbmax))
        #print('Contour generated')
    print("time = ",round((t+1)*dt,4),"\n")
var = int(round(nt/time_step))
system('gnuplot -e "var=\'%d\';cbmin=\'%f\';cbmax=\'%f\';t_s=\'%d\'" animation.gp'%(var,cbmin,cbmax,time_step))
end = time.time()
print("\n\n\nTotal Time taken =",end-start,"seconds\n\n\n")