#BARS 1
#The following routine is for the finite element solution of the free vibration of a
#bar with a one dof per node, three noded element, and a constant area per
#element for the eigenmode and the eigenvalue.
#-------------------------------------------------------------------------------------
import numpy as np
import math

#initializations
n=150
#number of elements
L=1
#lenght of rod
t_nod=2*(n+1)
#fixedfree case
Fixeddof=1
inter=L/n
y=np.linspace(inter/2,L-inter/2,n).transpose()
E=(210000000000)*np.ones(n)
#youngs modulus
Rho=7800*np.ones(n) #density
Modeno=3;
#modeshape found
PI=math.pi
A=np.exp( 5+2*y*(np.sin(2*PI*y/L)) )*0.000001
Mass=np.einsum('i,j->j', Rho,inter*A)  #same output as sum(Rho*inter.*A);
