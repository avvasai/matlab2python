#BARS 1
#The following routine is for the finite element solution of the free vibration of a
#bar with a one dof per node, three noded element, and a constant area per
#element for the eigenmode and the eigenvalue.
#-------------------------------------------------------------------------------------
import numpy as np
import math
from scipy.sparse import csc_matrix


#FUNCTION 1
def fp(L,E,Rho,normA,Modeno,Fixeddof):
	#formation of elements
	n=len(E)
	t_dof=2*n+1
	Le=L/n
	#Mass matrix
	Me=np.array([[4,2,-1],[2,16,2],[-1,2,4]])
	Me=Me*Le/30
	#Stifness matrix
	Ke=np.array([[7,-8,1],[-8,16,-8],[1,-8,7]])
	Ke=Ke/(3*Le)
	#Assembly
	M=csc_matrix((t_dof,t_dof))
	K=csc_matrix((t_dof,t_dof))

	for ele in range(1,n+1):
		#no clue what is happenning here atm
		
	
















#DRIVER CODE-------------------------------------------------

#initializations
n=150
#number of elements
L=1
#lenght of rod
t_nod=2*n+1
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
Mass=np.einsum('i,j->j', Rho,inter*A)
normA=A/(np.amax(A))

#ADD FUNCTIONS HERE
#FUNCTION CALL 1--- generating synthetic data

#FUNCTION CALL 2--- solving the inverse mode shape problem

#fixing the scaling of the c/s profile
sum_iter_2=np.einsum('i,j->j', Rho,inter*normI_A)
I_A=(Mass/sum_iter_2)*normI_A
